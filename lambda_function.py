import boto3
import pandas as pd
import io
import json
from datetime import datetime
from decimal import Decimal  # Import Decimal to handle float storage in DynamoDB

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StockDataResults')  # Table name must match what you created

def lambda_handler(event, context):
    try:
        print("🚀 Lambda function started")

        # Extract bucket name and file name from S3 event trigger
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        print(f"📂 File received: {file_key} in bucket: {bucket_name}")

        # Initialize S3 client
        s3 = boto3.client('s3')

        # Get the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        print("✅ File read successfully")

        # Load CSV into Pandas
        df = pd.read_csv(io.StringIO(file_content))
        print("📊 CSV file loaded into Pandas")

        # Ensure correct column names (skip first two rows if necessary)
        df = df.iloc[2:].reset_index(drop=True)
        df.columns = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

        # Convert price columns to numeric
        numeric_columns = ['Adj Close', 'Close', 'High', 'Low', 'Open']
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
        print("🔢 Converted columns to numeric values")

        # Compute the average closing price
        avg_close_price = df['Close'].mean()
        print(f"📈 Average Closing Price Calculated: {avg_close_price:.2f}")

        # Convert float to Decimal for DynamoDB
        avg_close_price_decimal = Decimal(str(round(avg_close_price, 2)))  # Convert float to Decimal

        # Store the result in DynamoDB
        table.put_item(
            Item={
                "file_key": file_key,  # Unique file identifier
                "timestamp": datetime.utcnow().isoformat(),  # Current processing timestamp
                "average_closing_price": avg_close_price_decimal,  # Converted Decimal value
                "status": "success"
            }
        )
        print(f"✅ Data stored in DynamoDB: {file_key}")

        # Construct a JSON response
        response_body = {
            "processed_file": file_key,
            "average_closing_price": str(avg_close_price_decimal),  # Convert Decimal back to string for JSON response
            "status": "success"
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    
    except Exception as e:
        print(f"❌ Error encountered: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e), "status": "failed"})
        }
