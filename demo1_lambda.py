import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('s3') #low-level functional API
    obj = client.get_object(Bucket='gz-demo-bucket1', Key='20230110/config.json')
    contents = obj['Body'].read()
    data = json.loads(contents)
    print(data["url"])
    print(data["username"])
    print("=========================")
    print(data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Executed reading S3 !')
    }
