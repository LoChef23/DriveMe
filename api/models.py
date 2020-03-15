import re
import random
import base64
import os
from passlib.apps import custom_app_context as pwd_context
import boto3
from flask_jwt_extended import create_access_token


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def validate_login(self):
        client = boto3.client('dynamodb')
        checkUserAttributes = client.get_item(
            TableName='Users',
            Key={
                'UserID': {'S': self.username}
            }
        )
        if 'Item' not in checkUserAttributes:
            validationErrorMessage = f'User {self.username} does not exists, please register the user first'
        elif not(pwd_context.verify(self.password, checkUserAttributes['Item']['UserPasswordHash']['S'])):
            validationErrorMessage = 'Wrong password'
        else:
            validationErrorMessage = ''
        
        return validationErrorMessage

    def generate_access_token(self):
        return create_access_token(identity=self.username)

class UserNotYetRegistered(User):

    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email

    def validate_registration_data(self):
        if self.username == '':
            validationErrorMessage = 'Please, insert a valid username'
        elif len(self.password) < 8:
            validationErrorMessage = 'Please, insert a valid password: password length should be at least 8 characters'
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            validationErrorMessage = 'Please, insert a valid email'
        else:
            validationErrorMessage = ''

        client = boto3.client('dynamodb')
        checkUser = client.get_item(
            TableName='Users',
            Key={
                'UserID': {'S': self.username}
            }
        )
        if 'Item' in checkUser:
            validationErrorMessage = f'User {self.username} exists already, please choose another username'
        else:
            validationErrorMessage = ''

        return validationErrorMessage
    
    def hash_password(self): 
        self.passwordHash = pwd_context.hash(self.password)
        return self.passwordHash        

    def insert_user_in_dynamodb(self):
        client = boto3.client('dynamodb')
        insertUser = client.put_item(
            TableName = 'Users',
            Item={
                'UserID':{'S': self.username},
                'UserEmail':{'S': self.email},
                'UserPasswordHash':{'S': self.passwordHash}
            }
        )
        return insertUser

class Question():
    def retrieve_random_question(self):
        client = boto3.client('dynamodb')
        tableDesc = client.describe_table(TableName='Questions')
        itemsInTable = 200
        questionRandomID = random.randint(1, itemsInTable)
        result = client.get_item(
            TableName='Questions',
            Key={
                'QuestionID': {'N': str(questionRandomID)}
            }
        )
        
        imageName = result['Item']['QuestionImage']['S']
        if imageName != '-':
            imagePath = os.path.join('images', imageName)
            with open(imagePath, 'rb') as imageToBeConverted:
                strQuestionImage = str(base64.b64encode(imageToBeConverted.read()))
        else:
            strQuestionImage = '-'

        return {
            'questionID': result['Item']['QuestionID']['N'],
            'questionText': result['Item']['QuestionText']['S'],
            'questionAnswer': result['Item']['isCorrect']['BOOL'],
            'questionImage': strQuestionImage
        }