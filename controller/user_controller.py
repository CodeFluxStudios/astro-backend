from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, Response
)
from model.standard_responses import (Unauthorized, StandardResponse)
import requests
import configparser
import json
from model.discord import Discord

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

userController = Blueprint('userApi', __name__, url_prefix='/api/user')
discord = Discord(config['BotData']['id'], config['BotData']['secret'], config['BotData']['token'])

@userController.route('')
def getUser():
    if 'token' in session:   
        response = discord.getUserResource('users/@me', session['token'])
        return StandardResponse(response)
    else:
        return Unauthorized

@userController.route('/guilds')
def getGuilds():
    if 'token' in session:   
        response = discord.getUserResource('users/@me/guilds', session['token'])
        return StandardResponse(response)
    else:
        return Unauthorized

@userController.route('/guilds/admin')
def getAdminGuilds():
    print()
    if 'token' in session:   
        response = discord.getUserResource('users/@me/guilds', session['token'])
        responseJson = json.loads(response)
        adminServers = []
        for server in responseJson:
            permssions = server["permissions"]
            admin = permssions & 8
            if admin == 8:
                adminServers.append(server)

        requestJson = json.dumps(adminServers)
        return StandardResponse(requestJson)
    else:
        return Unauthorized