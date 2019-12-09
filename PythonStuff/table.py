class Table:
    def __init__(self, deck):
        self.NW = []
        self.N = [deck.pop()]
        self.NE = []
        self.W = [deck.pop()]
        self.E = [deck.pop()]
        self.SW = []
        self.S = [deck.pop()]
        self.SE = []
        self.Deck = deck
