import boto3
from flask import Flask
from flask_restplus import Resource, Api
import random

client = boto3.client('dynamodb')
tableDesc = client.describe_table(TableName='Questions')
itemsInTable = int(tableDesc['Table']['ItemCount'])

app = Flask(__name__)
api = Api(app,version='0.1',
              title='DriveMe',
              description='App for anyone who wants to make some practice with some simple Quizzes in order to prepare the Driving License exam')

@api.route('/question/')
class Question(Resource):
    def get(self):
        questionRandomID = random.randint(1, itemsInTable)
        result = client.get_item(
            TableName='Questions',
            Key={
                'QuestionID': {'N': str(questionRandomID)}
            }
        )
        print(result)
        response = {}
        response['Question'] = {}
        response['Question']['ID'] = result['Item']['QuestionID']['N']
        response['Question']['Text'] = str(result['Item']['QuestionText']['S'])
        if result['Item']['QuestionExplanation']['S'] != '-':
            response['Question']['Explanation'] = result['Item']['QuestionExplanation']['S']
        if result['Item']['QuestionImage']['S'] != '-':
            response['Question']['Image'] = result['Item']['QuestionImage']['S']
        return response

if __name__ == '__main__':
    app.run()