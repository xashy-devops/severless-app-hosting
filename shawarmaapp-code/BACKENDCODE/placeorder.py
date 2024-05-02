import json
import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Orders')
    
    # Parse the input data
    try:
        data = json.loads(event['body'])
        order_id = str(uuid.uuid4())
        email = data['email']
        username = data['username']
        order_details = data['orderDetails']
        order_status = 'pending'
        order_date = datetime.now().isoformat()
    except KeyError as e:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Missing key in the input data: {}'.format(e)})
        }

    # Insert the new order into the Orders table
    try:
        table.put_item(Item={
            'OrderId': order_id,
            'Email': email,
            'Username': username,
            'OrderDetails': order_details,
            'OrderStatus': order_status,
            'OrderDate': order_date
        })
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
    
    # Return a success response
    return {
        'statusCode': 201,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Enable CORS
        },
        'body': json.dumps({'message': 'Order placed successfully', 'orderId': order_id})
    }
