import boto3

client = boto3.client('dynamodb')

try:
    usersTable = client.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'UserID',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'UserID',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
    
        }
    )
except:
   tableDescription = client.describe_table(TableName='Users')
   if tableDescription['Table']['TableStatus'] == 'ACTIVE':
       print('Table already created')
else:
    tableDescription = client.describe_table(TableName='Users')
    if tableDescription['Table']['TableStatus'] == 'CREATING':
       print('Creation of the table in progress')