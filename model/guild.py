
class Guild(object):

    def __init__(self, json):
        self.__dict__ = json.loads(json)