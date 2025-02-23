import json
import boto3
from botocore.exceptions import ClientError

# create lambda function thet create new item in dynamodb table

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('quiz')


def lambda_handler(event, context):
    try:
        print(event)
        item = json.loads(event['body'])
        print(item)
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Item created successfully',
                'id': item['id']  # Return the item ID
            })
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error creating item', 'error': str(e)})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid JSON'})
        }