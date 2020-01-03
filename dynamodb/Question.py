import boto3

class Question():

    def __init__(self, questionID, questionText, questionExplanation, questionImage, isCorrect):
        self.questionID = questionID
        self.questionText = questionText
        self.questionExplanation = questionExplanation
        self.questionImage = questionImage
        self.isCorrect = isCorrect

    def import_in_dynamodb(self):
        client = boto3.client('dynamodb')
        importQuestion = client.put_item(
            TableName = 'Questions',
            Item={
                'QuestionID':{'N': self.questionID},
                'QuestionText':{'S': self.questionText},
                'QuestionExplanation':{'S': self.questionExplanation},
                'QuestionImage':{'S': self.questionImage},
                'isCorrect':{'BOOL': self.isCorrect}
            }
        )