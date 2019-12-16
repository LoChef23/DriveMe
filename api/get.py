import boto3
from flask import Flask
from flask_restplus import Resource, Api
import random

client = boto3.client('dynamodb')
tableDesc = client.describe_table(TableName='Questions')
itemsInTable = int(tableDesc['Table']['ItemCount'])

app = Flask(__name__)
api = Api(app)

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
        response = result['Item']
        return response

if __name__ == '__main__':
    app.run(debug=True)