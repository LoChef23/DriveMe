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

        #validations: this part could be improved
        registrationValidationErrorMessage = userToBeRegistered.validate_registration()
        if registrationValidationErrorMessage != '':
            return {"validationError": registrationValidationErrorMessage}
        else:
            registrationCheckForUserExistence = userToBeRegistered.check_user_existence()
            if registrationCheckForUserExistence != '':
                return {"validationError": registrationCheckForUserExistence}

        try:
            passwordHash = userToBeRegistered.hash_password()
            access_token = userToBeRegistered.generate_access_token()
            usertInsertion = userToBeRegistered.insert_user_in_dynamodb()
            return {
                "message": f"User {userToBeRegistered.username} successfully registered",
                "accessToken": access_token
            }
        except:
            return {
            "message":f"Something went wrong"
            }, 500

class UserLogin(Resource):
    def post(self):
        loginData = loginParser.parse_args()

        userToLogin = User(loginData['username'], loginData['password'])

        #validations: this part could be improved
        loginValidationErrorMessage = userToLogin.validate_login()
        if loginValidationErrorMessage != '':
            return {"validationError": loginValidationErrorMessage}
        
        try:
            access_token = userToLogin.generate_access_token()
            return {
                "message": f"User {userToLogin.username} successfully logged in",
                "accessToken": access_token
            }
        except:
            return {
            "message":f"Something went wrong"
            }, 500

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}