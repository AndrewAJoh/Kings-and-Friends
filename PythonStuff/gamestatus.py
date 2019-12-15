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
    currentPlayer = 0
    playerList = []
    table = Table(createDeck())
    

#Serialize will convert all global variables to json so it can be sent back
def Serialize():
    activeGameJSON = json.dumps(GameStatus.isGameActivated, indent=4)
    currentPlayerJSON = json.dumps(GameStatus.currentPlayer, indent=4)
    playerListJSON = json.dumps(GameStatus.playerList, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    tableValue = [GameStatus.table.NW, GameStatus.table.N, GameStatus.table.NE, GameStatus.table.W, GameStatus.table.E, GameStatus.table.SW, GameStatus.table.S, GameStatus.table.SE] 
    tableJSON = json.dumps(tableValue, default=lambda o: str(o.value) + o.suit, indent=4)
    tableDeckJSON = json.dumps(GameStatus.table.Deck, default=lambda o: o.string, indent=4)
    resultJSON = activeGameJSON + currentPlayerJSON + playerListJSON + tableJSON + tableDeckJSON
    
    return resultJSON
