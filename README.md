# AWS-Stock-Data-Processor
A simple serverless AWS Lambda pipeline that automatically processes stock price data from S3 and stores results in DynamoDB
# 📊 AWS Stock Data Processor - Serverless Pipeline  

## 🚀 Overview  
This AWS project automates stock data processing using **Lambda, S3, and DynamoDB**.  
Whenever a new stock data file is uploaded to S3, a **Lambda function is triggered** to:  
✅ **Read the CSV file from S3**  
✅ **Process & clean the data using Pandas**  
✅ **Compute the average closing price**  
✅ **Store the results in DynamoDB for real-time access**  

---
🛠️ Technologies Used:
- **AWS Lambda (serverless data processing)**
- **Amazon S3 (storage & event triggers)**
- **Amazon DynamoDB (NoSQL database for storing results)**
- **Python (Pandas for data analysis)**
- **IAM Roles & Policies (AWS permissions setup)**

---
Setup & Deployment:
- **AWS S3 Setup**: Create an S3 bucket and upload stock CSV files
- **AWS Lambda Setup**: Deploy the Lambda function (Python script provided)
- **AWS IAM Roles**: Set up IAM roles & permissions to allow Lambda to read S3 and write to DynamoDB
- **AWS DynamoDB**: Create a DynamoDB table to store processed results
- **Testing**: Upload new stock data to S3 → Check logs in CloudWatch → Verify results in DynamoDB
---
## 🔹 Key Features
- ✅ **Event-Driven Processing**: AWS Lambda function triggers automatically when a new CSV file is uploaded to an S3 bucket.
- ✅ **Data Transformation**: The Lambda function reads the stock data, converts numeric columns, and computes the **average closing price**.
- ✅ **Cloud Storage & Database**: Raw stock data is stored in **Amazon S3**, and the processed results are stored in **Amazon DynamoDB**.
- ✅ **Logging & Monitoring**: AWS CloudWatch tracks Lambda execution logs and errors.
- ✅ **Security & Access Control**: IAM roles and policies grant necessary permissions to Lambda for accessing S3 and DynamoDB.
---
📊 Example Output:
- File received: googl_data_2020_2025.csv
- Average Closing Price Calculated: 119.08
- Data stored in DynamoDB successfully.


