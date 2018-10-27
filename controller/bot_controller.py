from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from model.standard_responses import (Unauthorized, StandardResponse, getAuthenticationJson, UnauthorizedJson, MissingAccessJson)
import requests
import configparser
import json
from model.discord import Discord
from random import randint
#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

botController = Blueprint('botApi', __name__, url_prefix='/api/bot', template_folder='../view')
discord = Discord(config['BotData']['id'], config['BotData']['secret'], config['BotData']['token'])

@botController.route('/guilds/<id>', methods=['GET'])
def getGuild(id):
    if 'token' in session:   
        response = discord.getBotResource('guilds/' + id)
        return StandardResponse(response)
    else:
        return Unauthorized


@botController.route('/guilds/oauth/<id>', methods=['GET'])
def joinGuild(id):
    if 'token' in session:   
        state = randint(100000, 999999)
        return  redirect(discord.generateAuthorizationUrl(config['Server']['baseurl'] + ':' + config['Server']['port'] + '/api/bot/guilds/callback', 'bot', state, 'guild_id=' + id + '&permissions=2146958839'))
    else:
        return Unauthorized



@botController.route('/guilds/callback')
def callbackAction():
    # Authorize to servers
    code = request.args.get('code')
    try:
        response = discord.authenticate(code, config['Server']['baseurl'] + ':' + config['Server']['port'] + '/api/bot/guilds/callback', 'bot')
        
        #Return JSON-Userdata to template
        if 'access_token' in response:
            data = {
                    'key': 'guild_auth',
                    'data': {
                        'guild_id': request.args.get('guild_id')
                    } 
                }
            return render_template('/backend/callback.html', response=data)
        
        return render_template('/backend/callback.html', response=UnauthorizedJson)
    except Exception as e:
        return render_template('/backend/callback.html', response=UnauthorizedJson)