

class GameState(object):

    def __init__(self, data):
        self.gameData = data
        self._food = None
        self._emptySpaces = None
        self._opponents = None
        self._myHead = None

    def opponents(self):
        if self._opponents is None:
            heads = []
            #TO DO: add all other snake heads to a vector or array