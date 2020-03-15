from flask import Flask
from flask_restful import Api
import resources, models
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = '\x0cS:7\xfb\xbd\x96A\xc6\xf8\x8a\xa8\xeeN7\xc8\r\n\xf3y<\x0c}A'
jwt = JWTManager(app)


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.QuestionToBeSent, '/question')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)