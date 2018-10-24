from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import requests
import configparser
import json

#Load Config
config = configparser.ConfigParser()
config.read('config.ini')

apiController = Blueprint('api', __name__, url_prefix='/api')

@apiController.route('/guilds')
def getGuilds():
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + session['token']})
        r = sess.get(config['Discord']['endpoint'] + 'users/@me/guilds')
        return str(json.dumps(r.json()))
    else:
        return redirect(url_for('login.loginAction'))

@apiController.route('/guilds/admin')
def getAdminGuilds():
    print()
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + session['token']})

        r = sess.get(config['Discord']['endpoint'] + 'users/@me/guilds')
        responseJson = json.loads(r.text)
        adminServers = []
        for server in responseJson:
            permssions = server["permissions"]
            admin = permssions & 8
            if admin == 8:
                adminServers.append(server)
        return str(json.dumps(adminServers))
    else:
        return redirect(url_for('login.loginAction'))

@apiController.route('/guilds/<id>')
def getGuild(id):
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bot ' + config['BotData']['bottoken']})
        print(config['BotData']['token'])
        r = sess.get(config['Discord']['endpoint'] + 'guilds/' + id)
        return str(json.dumps(r.json()))
    else:
        return redirect(url_for('login.loginAction'))

@apiController.route('/user')
def getUser():
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + session['token']})
        r = sess.get(config['Discord']['endpoint'] + 'users/@me')
        return str(json.dumps(r.json()))
    else:
        return redirect(url_for('login.loginAction'))