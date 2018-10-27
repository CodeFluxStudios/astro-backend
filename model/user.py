from model.discord_request import DiscordRequest, AuthType

class User:
    
    def __init__(self, token):
        self.token = token

    def getAccountInformation(self):
        DiscordRequest.getResource(AuthType.Bearer, self.token, '/user/@me')