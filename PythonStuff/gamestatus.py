import json
from table import Table
from card import Card
import random
from flask import Flask, jsonify

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
    turn = 0
    playerList = []
    table = Table(createDeck())
    gameWinners = {}
    activePlayers = 0
    spectatorSockets = []
    playerSockets = []
    
    

#Serialize will convert all global variables to json so it can be sent back
def Serialize(pid):
    activeGameJSON = json.dumps(GameStatus.isGameActivated)
    activeGameDict = json.loads(activeGameJSON)
    
    currentPlayerJSON = json.dumps(GameStatus.currentPlayer)
    currentPlayerDict = json.loads(currentPlayerJSON)
    
    playerJSON = json.dumps(GameStatus.playerList, default=lambda o: o.__dict__, sort_keys=True)
    playerDict = json.loads(playerJSON)
    #hide values we don't want other players to see
    for i in range(len(GameStatus.playerList)):
        playerDict[i]["numcards"] = len(GameStatus.playerList[i].hand)
        del playerDict[i]["hand"]
        del playerDict[i]["socketId"]

    handJSON = json.dumps(GameStatus.playerList[pid].hand, default=lambda o: o.__dict__, sort_keys=True)
    handDict = json.loads(handJSON)
    
    tableValue = {}
    tableValue["NW"] = GameStatus.table.NW
    tableValue["N"] = GameStatus.table.N
    tableValue["NE"] = GameStatus.table.NE
    tableValue["W"] = GameStatus.table.W
    tableValue["E"] = GameStatus.table.E
    tableValue["SW"] = GameStatus.table.SW
    tableValue["S"] = GameStatus.table.S
    tableValue["SE"] = GameStatus.table.SE
    tableJSON = json.dumps(tableValue, default=lambda o: str(o.value) + o.suit)
    tableDict = json.loads(tableJSON)
    
    tableDeckJSON = json.dumps(GameStatus.table.Deck, default=lambda o: o.string)
    tableDeckDict = json.loads(tableDeckJSON)

    gameWinnersJSON = json.dumps(GameStatus.gameWinners, default=lambda o: o.string)
    gameWinnersDict = json.loads(gameWinnersJSON)
    
    dictionary = {'ActiveGame': activeGameDict, 'CurrentPlayer': currentPlayerDict, 'Player': playerDict, 'Hand': handDict, 'Table' : tableDict, 'Deck': tableDeckDict, 'Winners' : gameWinnersDict}

    final = json.dumps(dictionary, indent=4)
    
    return final

def SerializeSpectator():
    activeGameJSON = json.dumps(GameStatus.isGameActivated)
    activeGameDict = json.loads(activeGameJSON)

    currentPlayerJSON = json.dumps(GameStatus.currentPlayer)
    currentPlayerDict = json.loads(currentPlayerJSON)

    playerJSON = json.dumps(GameStatus.playerList, default=lambda o: o.__dict__, sort_keys=True)
    playerDict = json.loads(playerJSON)
    #hide values we don't want other players to see
    for i in range(len(GameStatus.playerList)):
        playerDict[i]["numcards"] = len(GameStatus.playerList[i].hand)
        del playerDict[i]["hand"]
        del playerDict[i]["socketId"]

    tableValue = {}
    tableValue["NW"] = GameStatus.table.NW
    tableValue["N"] = GameStatus.table.N
    tableValue["NE"] = GameStatus.table.NE
    tableValue["W"] = GameStatus.table.W
    tableValue["E"] = GameStatus.table.E
    tableValue["SW"] = GameStatus.table.SW
    tableValue["S"] = GameStatus.table.S
    tableValue["SE"] = GameStatus.table.SE
    tableJSON = json.dumps(tableValue, default=lambda o: str(o.value) + o.suit)
    tableDict = json.loads(tableJSON)

    tableDeckJSON = json.dumps(GameStatus.table.Deck, default=lambda o: o.string)
    tableDeckDict = json.loads(tableDeckJSON)

    gameWinnersJSON = json.dumps(GameStatus.gameWinners, default=lambda o: o.string)
    gameWinnersDict = json.loads(gameWinnersJSON)

    dictionary = {'ActiveGame': activeGameDict, 'CurrentPlayer': currentPlayerDict, 'Player': playerDict, 'Table' : tableDict, 'Deck': tableDeckDict, 'Winners' : gameWinnersDict}

    final = json.dumps(dictionary, indent=4)

    return final
