import os
import configparser


config = configparser.ConfigParser()

config['Security'] = {}
config['Security']['secretkey'] = str(os.urandom(16))

config['Server'] = {}
config['Server']['baseurl'] = 'http://lvh.me'
config['Server']['port'] = '5000'

config['Discord'] = {}
config['Discord']['endpoint'] = 'https://discordapp.com/api/'
config['Discord']['token'] = 'oauth2/token'

config['BotData'] = {}
config['BotData']['id'] = 'BotIdHere'
config['BotData']['secret'] = 'BotSecretHere'
config['BotData']['token'] = 'BotTokenHere'

with open('config.ini', 'w') as configfile:
    config.write(configfile)

