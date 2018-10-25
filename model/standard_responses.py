import json
from flask import Response
UnauthorizedJson = { "error": 40001,
                     "message": 'Unauthorized'}

ForbiddenJson = { "error": 40003, 
                  "message": 'Forbidden'}

MissingAccessJson = { "error": 50001, 
                  "message": 'Missing access'}

Unauthorized = json.dumps(UnauthorizedJson), 401
Forbidden = json.dumps(ForbiddenJson), 403


class StandardResponse(Response):
    def __init__(self,json):
            Response.__init__(self,json, 201)
            self.headers['Content-type'] = 'application/json'


def getAuthenticationJson(code, config):
    return {
        'client_id': config['BotData']['id'],
        'client_secret': config['BotData']['secret'],
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': config['Server']['baseurl'] + ':' + config['Server']['port'] + '/callback',
        'scope': 'identify email connections guilds'
    }