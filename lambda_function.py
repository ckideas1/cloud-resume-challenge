import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitorCount')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'counter'},
        UpdateExpression='SET visits = visits + :incr',
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'visits': int(response['Attributes']['visits'])})
    }
