import requests
import json   
from enum import Enum

class AuthType(Enum):
    Bearer = 'Bearer'
    Bot = 'Bot'

class DiscordRequest:
    @staticmethod
    def getResource(authType : AuthType,  access_token, resource, endpoint = 'https://discordapp.com/api/'):
        sess = requests.Session()
        sess.headers.update({'Authorization': authType.value + " " + access_token})
        request = sess.get(endpoint + resource)
        return ((request.json()))