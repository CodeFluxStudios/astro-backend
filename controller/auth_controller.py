from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import requests
import configparser
import json
from random import randint
from model.discord import Discord
from model.standard_responses import (Forbidden, Unauthorized)

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

authController = Blueprint('auth', __name__, url_prefix='/auth', template_folder='../view')
scopes='identify email connections guilds'
discord = Discord(config['BotData']['id'], config['BotData']['secret'], config['BotData']['token'])

@authController.route('/login')
def loginAction():
    state = randint(100000, 999999)
    return redirect(discord.generateAuthorizationUrl(config['Server']['baseurl'] + ':' + config['Server']['port'] + '/auth/callback', scopes, state))

@authController.route('/session')
def sessionAction():
    if 'token' in session:
        return 'Logged in as %s' % (session['token'])
    return 'You are not logged in'

@authController.route('/callback')
def callbackAction():
    # Authorize to servers
    code = request.args.get('code')

    try:
        response = discord.authenticate(code, config['Server']['baseurl'] + ':' + config['Server']['port'] + '/auth/callback', scopes)
        if 'access_token' not in response:
            return render_template('/backend/callback.html', response=response)

        session['token'] = response["access_token"]

        #Return JSON-Userdata to template
        r = discord.getUserResource('users/@me', session['token'])
        data = {
            'key': 'user_auth',
            'data': json.loads(r)
        }
        return render_template('/backend/callback.html', response=data)

    except requests.exceptions.HTTPError as e:
        return e.response()

@authController.route('/logout')
def logoutAction():
    if 'token' in session:
        session.clear()
        return 'Logged out'
    else:
        return 'You are not logged in'
