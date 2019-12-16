import boto3

client = boto3.client('dynamodb')

try:
    questionsTable = client.create_table(
        TableName='Questions',
        KeySchema=[
            {
                'AttributeName': 'QuestionID',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'QuestionID',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
    
        }
    )
except:
   tableDescription = client.describe_table(TableName='Questions')
   if tableDescription['Table']['TableStatus'] == 'ACTIVE':
       print('Table already created')
else:
    tableDescription = client.describe_table(TableName='Questions')
    if tableDescription['Table']['TableStatus'] == 'CREATING':
       print('Creation of the table in progress')