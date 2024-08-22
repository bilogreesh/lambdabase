import json
import boto3
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = os.environ['SQS_QUEUE_URL']
    #https://sqs.us-east-1.amazonaws.com/533267111290/pet-order-queue
    # Message to send
    message_body = 'Hello, this is a message from Lambda!'
    
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS!')
    }
