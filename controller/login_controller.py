from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import requests
import configparser
import json
from random import randint

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

loginController = Blueprint('login', __name__, url_prefix='', template_folder='../view')

@loginController.route('/login')
def loginAction():
    state = randint(100000, 999999)
    return redirect('https://discordapp.com/oauth2/authorize?response_type=code&client_id=' + 
    config['BotData']['BotId'] + '&scope=identify email connections guilds&state=' + str(state) + '&redirect_uri=' + config['Server']['baseurl'] + ':' + config['Server']['port'] + '/callback')
    

@loginController.route('/session')
def sessionAction():
    if 'token' in session:
        return 'Logged in as %s' % (session['token'])
    return 'You are not logged in'

@loginController.route('/callback')
def callbackAction():
    # Authorize to servers
    code = request.args.get('code')
    data = {
        'client_id': config['BotData']['BotId'],
        'client_secret': config['BotData']['BotSecret'],
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config['Server']['baseurl'] + ':' + config['Server']['port'] + '/callback',
        'scope': 'identify email connections guilds'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(config['Discord']['endpoint'] + config['Discord']['token'], data, headers)
    r.raise_for_status()
    jsonData = r.json()
    session['token'] = jsonData["access_token"]

    #Return JSON-Userdata to template
    sess = requests.Session()
    sess.headers.update({'Authorization': 'Bearer ' + session['token']})
    r = sess.get(config['Discord']['endpoint'] + 'users/@me')

    return render_template('/backend/callback.html', response=r.json())

@loginController.route('/logout')
def logoutAction():
    if 'token' in session:
        session.clear()
        return 'Logged out'
    else:
        return 'You are not logged in'
