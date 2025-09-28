# Event-Driven AWS Lambda Project Using Terraform

## Project Overview

This project demonstrates an event-driven architecture on AWS using Lambda, S3, and DynamoDB, with infrastructure defined via Terraform. The Lambda function processes files uploaded to S3, stores metadata in DynamoDB, and showcases best practices in cloud architecture.

While this project focuses on local/cloud architecture and IaC, all components are fully functional and tested without CI/CD deployment.

## Project Highlights

- **AWS Lambda Function**: Triggered by S3 object uploads, written in Python 3.13.

- **S3 Bucket Integration**: Monitors file uploads and triggers the Lambda.

- **DynamoDB Table**: Stores file metadata for tracking and processing.

- **Terraform Infrastructure**: All resources are defined as code for reproducibility.

- **Event-Driven Workflow**: Demonstrates serverless triggers and data flow.

- **Local Testing**: Lambda function tested locally using sample S3 events.

# Architecture Diagram

(Optional: insert a simple diagram of S3 → Lambda → DynamoDB flow here)

# Skills Demonstrated

Designing and implementing event-driven architectures on AWS

Working with Lambda, S3, IAM roles, and DynamoDB

Writing Infrastructure-as-Code with Terraform

Local testing and debugging of serverless workflows

Understanding AWS resource references and permissions

Local Testing Instructions

Ensure AWS CLI is configured with access to your account.

Zip the Lambda function:

cd lambda
zip function.zip lambda_function.py


Invoke Lambda locally with a test event:

aws lambda invoke \
  --function-name file-processor \
  --payload file://event.json \
  output.json


Check output.json for results.

Project Structure
aws-data-pipeline/
├─ lambda/
│  ├─ lambda_function.py
│  └─ function.zip
├─ terraform/
│  └─ main.tf
├─ event.json
├─ README.md
