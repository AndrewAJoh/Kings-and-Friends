class Player:
    def __init__(self, name, playerId, socketId):
        super().__init__()
        self.name = name
        self.hand = []
        self.isTurn = False
        self.playerId = playerId
        self.socketId = socketId
