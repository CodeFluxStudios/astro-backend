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

@apiController.route('/servers')
def getServers():
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + session['token']})
        r = sess.get(config['Discord']['endpoint'] + 'users/@me/guilds')
        return str(r.text)
    else:
        return redirect(url_for('login.loginAction'))

@apiController.route('/user')
def getUser():
    if 'token' in session:   
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + session['token']})
        r = sess.get(config['Discord']['endpoint'] + 'users/@me')
        return str(r.text)
    else:
        return redirect(url_for('login.loginAction'))

    