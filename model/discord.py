import requests
import json
from model.standard_responses import (UnauthorizedJson, ForbiddenJson)

class Discord:

    def __init__(self, id, secret, token, endpoint = 'https://discordapp.com/api/'):
        self.endpoint = endpoint
        self.id = id
        self.secret = secret
        self.token = token

    def getAuthenticationJson(self, code, redirect_uri, scope):
        return {
            'client_id': self.id,
            'client_secret': self.secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'scope': scope
        }
    

    def getAuthenticationHeader(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return headers

    def authenticate(self, code, redirect_uri, scope):
        try:
            data = self.getAuthenticationJson(code, redirect_uri, scope)
            headers = self.getAuthenticationHeader()
            req = requests.post(self.endpoint + 'oauth2/token', data, headers)
            response = json.dumps((req.json()))
            if 'error' in response:
                return {
                    '401': UnauthorizedJson,
                    '403': ForbiddenJson
                }.get(response, req.json())
            else:
                return req.json()
        except Exception as e:
            raise(e)
    
    def getUserResource(self, resource, access_token):
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bearer ' + access_token})
        request = sess.get(self.endpoint + resource)

        requestJson = json.dumps(request.json())
        return (requestJson)

    def getBotResource(self, resource):
        sess = requests.Session()
        sess.headers.update({'Authorization': 'Bot ' + self.token})
        request = sess.get(self.endpoint + resource)

        requestJson = json.dumps(request.json())
        return (requestJson)
    
    def generateAuthorizationUrl(self, redirect_uri, scopes, state, addition = ''):
            return str('https://discordapp.com/oauth2/authorize?response_type=code&client_id=' + 
            self.id + '&scope=' + scopes + '&state=' + str(state) + '&redirect_uri=' + redirect_uri + "&" + addition)
