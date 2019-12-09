class Card:
    def __init__(self, value, suit, color):
        super().__init__()
        self.value = value
        self.suit = suit
        self.color = color
        self.position = int
    def __str__(self):
        return str(self.suit)+str(self.value)
