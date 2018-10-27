from model.discord_request import DiscordRequest, AuthType
from model.guild import Guild

class Bot:
    def __init__(self, token):
        self.token = token

    def getGuild(self, id):
        resource = DiscordRequest.getResource(AuthType.Bot, self.token, 'guilds/' + str(id))
        if 'code' in resource:
            return None
        else:
            joined = {'bot_joined': True}
            resource.update(joined)
            return Guild(resource)

    def getBotJoinedGuild(self,id):
        resource = DiscordRequest.getResource(AuthType.Bot, self.token, 'guilds/' + str(id))
        if 'code' in resource:
            return False
        else:
            return True