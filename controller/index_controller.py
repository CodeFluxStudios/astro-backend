from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import send_from_directory
import requests
import configparser
import json

indexController = Blueprint('index', __name__, url_prefix='/', static_folder='../view')

@indexController.route('/')
def routeAction():
    #if 'token' in session:
    return send_from_directory(indexController.static_folder, 'index.html')
    #return 'You are not logged in'

@indexController.route('/<path:path>')
def routeActionPar(path):
    #if 'token' in session:
    return send_from_directory(indexController.static_folder, path)
    #return 'You are not logged in'
