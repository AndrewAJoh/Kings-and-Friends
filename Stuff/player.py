class Player:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hand = []
        self.isTurn = False
