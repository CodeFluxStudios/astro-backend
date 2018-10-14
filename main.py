
from controller.login_controller import loginController
from controller.api_controller import apiController
from flask import (app, Flask)
import os
import configparser

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

#Configure app
app = Flask(__name__)
app.register_blueprint(loginController)
app.register_blueprint(apiController)
app.secret_key = config['Security']['SecretKey']

#Run app
app.run()
