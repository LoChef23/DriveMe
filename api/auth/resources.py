from flask_restful import Resource, reqparse
from models import User, UserNotYetRegistered

loginParser = reqparse.RequestParser()
loginParser.add_argument('username', help='This field could not be empty', required=True)
loginParser.add_argument('password', help='This field could not be empty', required=True)

registrationParser = loginParser.copy()
registrationParser.add_argument('email', help='This field could not be empty', required=True)

class UserRegistration(Resource):
    def post(self):
        registrationData = registrationParser.parse_args()

        userToBeRegistered = UserNotYetRegistered(registrationData['username'], registrationData['password'], registrationData['email'])
        
        #this part could be improved
        userValidationErrorMessage = userToBeRegistered.validate_user()
        if userValidationErrorMessage != '':
            return {"validationError": userValidationErrorMessage}
        else:
            userEmailValidationErrorMessage = userToBeRegistered.validate_user_email()
            if userEmailValidationErrorMessage != '':
                return {"validationError": userEmailValidationErrorMessage}
        
        passwordHash = userToBeRegistered.hash_password()

        # check if user is already existing with that username first

        usertInsertion = userToBeRegistered.insert_user_in_dynamodb()

        return usertInsertion

class UserLogin(Resource):
    def post(self):
        loginData = loginParser.parse_args()
        return loginData

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}