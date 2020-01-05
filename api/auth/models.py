import re
from passlib.apps import custom_app_context as pwd_context
import boto3


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def validate_user(self):
        if self.username == '':
            validationErrorMessage = 'Please, insert a valid username'
        elif len(self.password) < 8:
            validationErrorMessage = 'Please, insert a valid password: password length should be at least 8 characters'
        else:
            validationErrorMessage = ''
        
        return validationErrorMessage


class UserNotYetRegistered(User):

    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email
    
    #this part could be improved
    def validate_user_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            validationErrorMessage = 'Please, insert a valid email'
        else:
            validationErrorMessage = ''
                        
        return validationErrorMessage 

    def hash_password(self):
        hashedPassword = pwd_context.hash(self.password)
        self.passwordHash = hashedPassword
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