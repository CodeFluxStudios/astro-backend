
from controller.auth_controller import authController
from controller.user_controller import userController
from controller.bot_controller import botController
from controller.index_controller import indexController
from flask import (app, Flask)
from flask import send_from_directory
import os
import configparser
from model.discord import Discord

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')
discord = Discord(config['BotData']['id'], config['BotData']['secret'], config['BotData']['token'])
#Configure app
app = Flask(__name__, static_folder='view')
app.register_blueprint(indexController)
app.register_blueprint(botController)
app.register_blueprint(userController)
app.register_blueprint(authController)

app.secret_key = config['Security']['secretkey']
#Run app
app.run()
