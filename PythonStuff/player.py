class Player:
    def __init__(self, name, playerId):
        super().__init__()
        self.name = name
        self.hand = []
        self.isTurn = False
        self.playerId = playerId
