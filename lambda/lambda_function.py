import json
import boto3
import os
from datetime import datetime

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Environment variables for table and topic
TABLE_NAME = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

def handler(event, context):
    print("Event:", json.dumps(event))

    # Parse S3 event
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    size = record['s3']['object']['size']

    # Save metadata in DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item={
        'id': key,
        'bucket': bucket,
        'size': size,
        'timestamp': datetime.utcnow().isoformat()
    })

    # Notify via SNS
    message = f"File {key} uploaded to {bucket}, size {size} bytes."
    sns.publish(TopicArn=TOPIC_ARN, Message=message)

    return {"status": "success", "file": key}

# Local testing block
if __name__ == "__main__":
    with open("event.json") as f:
        test_event = json.load(f)
    print("Running Lambda locally...")
    result = handler(test_event, None)
    print("Lambda result:", result)
