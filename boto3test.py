import boto3

client = boto3.client('dynamodb')

try:
    questionsTable = client.create_table(
        TableName='Questions2',
        KeySchema=[
            {
                'AttributeName': 'question2ID',
                'KeyType': 'HASH'  #Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'question2ID',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except:
    response = client.describe_table(
    TableName='Questions2'
    )
    print(response)
else:
    response = client.describe_table(
    TableName='Questions2'
    )
    print(response)
