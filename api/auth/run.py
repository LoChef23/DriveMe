from flask import Flask
from flask_restful import Api
import resources, models, views


app = Flask(__name__)
api = Api(app)


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    app.run(debug=True)