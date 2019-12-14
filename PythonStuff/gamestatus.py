import json
from table import Table
from card import Card
import random

def createDeck():
    # Creates and shuffles 52-card deck
    deck = []
    for i in range(13):
        deck.append(Card(i + 1, "H", "R"))
        deck.append(Card(i + 1, "D", "R"))
        deck.append(Card(i + 1, "C", "B"))
        deck.append(Card(i + 1, "S", "B"))
        random.shuffle(deck)
    return deck

#GameStatus will have all relevant global objects we need for the lifetime of a game
class GameStatus:
    isGameActivated = False
    playerList = []
    table = Table(createDeck())
    

#Serialize will convert all global variables to json so it can be sent back
def Serialize():
    final1 = json.dumps(GameStatus.playerList, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    tablevalue = [GameStatus.table.NW, GameStatus.table.N, GameStatus.table.NE, GameStatus.table.W, GameStatus.table.E, GameStatus.table.SW, GameStatus.table.S, GameStatus.table.SE] 
    final2 = json.dumps(tablevalue, default=lambda o: str(o.value) + o.suit, indent=4)
    final3 = json.dumps(GameStatus.table.Deck, default=lambda o: str(o.value) + o.suit, indent=4)
    final = final1 + final2 + final3
    return final
