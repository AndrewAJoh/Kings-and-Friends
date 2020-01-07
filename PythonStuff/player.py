class Player:
    def __init__(self, name, playerId, socketId):
        super().__init__()
        self.name = name
        self.hand = []
        self.isTurn = False
        self.inGame = True
        self.playerId = playerId
        self.socketId = socketId
