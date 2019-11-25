import boto3
import time
import json

client = boto3.client('dynamodb')
tableName = 'Questions'
#existingTables = client.list_tables()['TableNames']

# if tableName in existingTables:
#     client.delete_table(TableName=tableName)
#     time.sleep(10)

# questionsTableResponse = client.create_table(
#     TableName='Questions',
#     KeySchema=[
#         {
#             'AttributeName': 'QuestionID',
#             'KeyType': 'HASH'
#         },
#     ],
#     AttributeDefinitions=[
#         {
#            'AttributeName': 'QuestionID',
#            'AttributeType': 'N'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 1,
#         'WriteCapacityUnits': 1
#     })

with open('questions.json') as jsonFile:
    questions = json.load(jsonFile)
    i = 0
    for question in questions:
        questionText = question['question']
        isCorrect = question['isCorrect']
        client.put_item(
            TableName=tableName,
            Item={
                'QuestionID': {'N': str(i)},
                'QuestionText': {'S': questionText},
                'IsCorrect':{'BOOL':isCorrect}
            }
        )
        i = i + 1
        