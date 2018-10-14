import os
import configparser


config = configparser.ConfigParser()

config['Security'] = {}
config['Security']['SecretKey'] = str(os.urandom(16))

config['Server'] = {}
config['Server']['baseurl'] = 'http://lvh.me'
config['Server']['port'] = '5000'

config['Discord'] = {}
config['Discord']['Endpoint'] = 'https://discordapp.com/api/'
config['Discord']['DiscordToken'] = 'oauth2/token'

config['BotData'] = {}
config['BotData']['BotId'] = 'BotIdHere'
config['BotData']['BotSecret'] = 'BotSecretHere'

with open('config.ini', 'w') as configfile:
    config.write(configfile)

