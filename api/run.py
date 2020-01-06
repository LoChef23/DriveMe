from flask import Flask
from flask_restful import Api
import resources, models
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.QuestionToBeSent, '/question')

if __name__ == '__main__':
    app.run(debug=True)