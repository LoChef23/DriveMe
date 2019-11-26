import json
import boto3

class Question():

    def __init__(self, questionID, questionText, isCorrect):
        self.questionID = questionID
        self.questionText = questionText
        self.isCorrect = isCorrect

    def import_in_dynamodb(self):
        client = boto3.client('dynamodb')
        importQuestion = client.put_item(
            TableName = 'Questions',
            Item={
                'QuestionID':{'N': self.questionID},
                'QuestionText':{'S': self.questionText},
                'isCorrect':{'BOOL': self.isCorrect}
            }
        )

with open('questions.json', 'r') as questionsFile:
    questionsList = json.load(questionsFile)

i = 1
for question in questionsList:
    if question['question'] != '' and type(question['isCorrect']) == bool:
        questionID = str(i)
        questionText = question['question']
        isCorrect = question['isCorrect']
        QuestionToBeImported = Question(questionID, questionText, isCorrect)
        QuestionToBeImported.import_in_dynamodb()
        i += 1
    else:
        print(f'Following question could not be imported:\n{question}')
        continue
print('Import completed')