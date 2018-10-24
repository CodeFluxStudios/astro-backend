
from controller.login_controller import loginController
from controller.api_controller import apiController
from controller.index_controller import indexController
from flask import (app, Flask)
from flask import send_from_directory
import os
import configparser

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

#Configure app
app = Flask(__name__, static_folder='view')
app.register_blueprint(loginController)
app.register_blueprint(apiController)
app.register_blueprint(indexController)

app.secret_key = config['Security']['secretkey']
#Run app
app.run()
