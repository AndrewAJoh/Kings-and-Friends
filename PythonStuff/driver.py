from player import Player
from card import Card
from table import Table
import random
from flask import request, Flask, jsonify, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import json
import sys
from gamestatus import GameStatus, Serialize, createDeck 
        
def createPlayer(playerName, socketId):
    playerId = len(GameStatus.playerList)
    player = Player(playerName, playerId, socketId)
    GameStatus.playerList.append(player)
    sys.stdout.write('There are now ' + str(len(GameStatus.playerList)) + ' players in the game' + '\n')
    sys.stdout.flush()
    if (len(GameStatus.playerList) == 4):
        startGame()

def startGame():
        sys.stdout.write("The game will now start\n")
        sys.stdout.flush()
        GameStatus.isGameActivated = True
        GameStatus.playerList[GameStatus.currentPlayerIndex].isTurn = True
        GameStatus.table.N = [GameStatus.table.Deck.pop()]
        GameStatus.table.W = [GameStatus.table.Deck.pop()]
        GameStatus.table.E = [GameStatus.table.Deck.pop()]
        GameStatus.table.S = [GameStatus.table.Deck.pop()]
        distributeCards(GameStatus.playerList, GameStatus.table.Deck)
        drawCard()
        sys.stdout.write("It is %s's turn" % GameStatus.playerList[GameStatus.currentPlayerIndex].name + '\n')
        sys.stdout.flush()


def distributeCards(playerArray, deck):
    # Distributes 7 cards to each player
    for player in playerArray:
        i = 0
        while i < 7:
            thisCard = deck.pop()
            thisCard.position = i
            player.hand.append(thisCard)
            i += 1

#Update card positions for the current player
def updateCardPositions():
    for i in range(len(GameStatus.playerList[GameStatus.currentPlayerIndex].hand)):
        GameStatus.playerList[GameStatus.currentPlayerIndex].hand[i].position = i
        

def placeCard(player, card, pile, table):
    # Takes input card from current player through button action, places card in desired pile.
    # Card will be a card object containing value, suit, and location in player hand list
    # Must contain logic for alternating black/red as well as being 1 value lower than previous
    response = {}
    if pile == "NW":
        if (not table.NW):
            if (int(card.value) != 13):
                response["error"] = "You must place a King in the corner first."
            else:
                table.NW.append(card)
                updateCardPositions()
        elif (table.NW[-1].color != card.color):
            if (card.value == table.NW[-1].value - 1):
                table.NW.append(card)
                updateCardPositions()
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "N":
        if (not table.N):
            table.N.append(card)
            updateCardPositions()
        else:
            if (table.N[-1].color != card.color):
                if (card.value == table.N[-1].value - 1):
                    table.N.append(card)
                    updateCardPositions()
                else:
                    response["error"] = "Wrong number."
            else:
                response["error"] = "Wrong color."
    elif pile == "NE":
        if (not table.NE):
            if (card.value != 13):
                response["error"] = "You must place a King in the corner first."
                return response
            else:
                table.NE.append(card)
                updateCardPositions()
        elif (table.NE[-1].color != card.color):
            if (card.value == table.NE[-1].value - 1):
                table.NE.append(card)
                updateCardPositions()
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "W":
        if (not table.W):
            table.W.append(card)
            updateCardPositions()
        else:
            if (table.W[-1].color != card.color):
                if (card.value == table.W[-1].value - 1):
                    table.W.append(card)
                    updateCardPositions()
                else:
                    response["error"] = "Wrong number."
            else:
                response["error"] = "Wrong color."
    elif pile == "E":
        if (not table.E):
            table.E.append(card)
            updateCardPositions()
        else:
            if (table.E[-1].color != card.color):
                if (card.value == table.E[-1].value - 1):
                    table.E.append(card)
                    updateCardPositions()
                else:
                    response["error"] = "Wrong number."
            else:
                response["error"] = "Wrong color."
    elif pile == "SW":
        if (not table.SW):
            if (card.value != 13):
                response["error"] = "You must place a King in the corner first."
                return response
            else:
                table.SW.append(card)
                updateCardPositions()
        elif (table.SW[-1].color != card.color):
            if (card.value == table.SW[-1].value - 1):
                table.SW.append(card)
                updateCardPositions()
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "S":
        if (not table.S):
            table.S.append(card)
            updateCardPositions()
        else:
            if (table.S[-1].color != card.color):
                if (card.value == table.S[-1].value - 1):
                    table.S.append(card)
                    updateCardPositions()
                else:
                    response["error"] = "Wrong number."
            else:
                response["error"] = "Wrong color."
    elif pile == "SE":
        if (not table.SE):
            if (card.value != 13):
                response["error"] = "You must place a King in the corner first."
                return response
            else:
                table.SE.append(card)
                updateCardPositions()
        elif (table.SE[-1].color != card.color):
            if (card.value == table.SE[-1].value - 1):
                table.SE.append(card)
                updateCardPositions()
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    return response

#Draw card for the current player
def drawCard():
    card = GameStatus.table.Deck.pop()
    card.position = len(GameStatus.playerList[GameStatus.currentPlayerIndex].hand)
    GameStatus.playerList[GameStatus.currentPlayerIndex].hand.append(card)

def movePile(pile, destination):
    response = {}
    # check if the pile to be moved is empty
    if len(getattr(GameStatus.table, pile)) == 0:
        response["error"] = "That pile is empty."
    else:
        # check if there are cards in destination pile
        if len(getattr(GameStatus.table, destination)) != 0:
            # check for opposite color rule
            if getattr(GameStatus.table, destination)[-1].color != getattr(GameStatus.table, pile)[0].color:
                # check for sequence rule
                if getattr(GameStatus.table, pile)[0].value == getattr(GameStatus.table, destination)[-1].value - 1:
                    # iterate through pile loop and remove cards, placing in destination list
                    while len(getattr(GameStatus.table, pile)) > 0:
                        getattr(GameStatus.table, destination).append(
                            getattr(GameStatus.table, pile).pop(0))
                else:
                    response["error"] = "Highest card is not one less than the last card in destination pile"
            else:
                response["error"] = "Highest card is not of opposite color to the last card in destination pile"
        else:
            # if there are no cards in destination, only kings can be put in corner
            if destination == "NW" or destination == "NE" or destination == "SW" or destination == "SE":
                # check if highest card is king
                if getattr(GameStatus.table, pile)[0].value == 13:
                    while len(getattr(GameStatus.table, pile)) > 0:
                        getattr(GameStatus.table, destination).append(
                            getattr(GameStatus.table, pile).pop(0))
                else:
                    response["error"] = "Only kings can start in the corner"
            else:
                # if not going in corner, can place any card
                while len(getattr(GameStatus.table, pile)) > 0:
                    getattr(GameStatus.table, destination).append(
                        getattr(GameStatus.table, pile).pop(0))
    return response
        
def endTurn(isPlayerLeaving):
    playerIds = []
    for i in range(len(GameStatus.playerList)):
        playerIds.append(GameStatus.playerList[i].playerId)
    GameStatus.playerList[GameStatus.currentPlayerIndex].isTurn = False
    if GameStatus.currentPlayerId == playerIds[len(playerIds)-1]:
        GameStatus.currentPlayerId = playerIds[0]
        GameStatus.currentPlayerIndex = 0
    else:
        GameStatus.currentPlayerIndex = playerIds.index(GameStatus.currentPlayerId)+1
        GameStatus.currentPlayerId = playerIds[GameStatus.currentPlayerIndex]
    if (isPlayerLeaving):
        GameStatus.currentPlayerIndex -= 1
        GameStatus.playerList[GameStatus.currentPlayerIndex].isTurn = True
    else:
        GameStatus.playerList[GameStatus.currentPlayerIndex].isTurn = True
        drawCard()

def endGame():
    sys.stdout.write("The game is over. " + GameStatus.playerList[GameStatus.currentPlayerIndex].name + " wins.\n")
    sys.stdout.flush()
    playerName = GameStatus.playerList[GameStatus.currentPlayerIndex].name
    if playerName in GameStatus.gameWinners.keys():
        GameStatus.gameWinners[playerName] += 1
    else:
        GameStatus.gameWinners[playerName] = 1
    
    #update final card layout
    for i in range(len(GameStatus.playerList)):
        response = Serialize(GameStatus.playerList[i].playerId)
        socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)
        
    responseDict = {}
    responseDict["winnerId"] = str(GameStatus.currentPlayerId)
    responseDict["winnerName"] = playerName
    
    for i in range(len(GameStatus.playerList)):
        response = json.dumps(responseDict)
        socketio.emit('game over', response, room = GameStatus.playerList[i].socketId)
        
    GameStatus.isGameActivated = False
    GameStatus.currentPlayerId = 0
    GameStatus.currentPlayerIndex = 0
    GameStatus.playerList = []
    GameStatus.table = Table(createDeck())

def endGameFromLackOfPlayers():
    sys.stdout.write("Not enough players to continue. The game is over. \n")
    sys.stdout.flush()
    GameStatus.isGameActivated = False
    GameStatus.currentPlayerId = 0
    GameStatus.currentPlayerIndex = 0
    GameStatus.playerList = []
    GameStatus.table = Table(createDeck())

#WebAPI
app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('join game')
def JoinGame(datainput, methods=['GET', 'POST']):
    responseDict = {}
    if (GameStatus.isGameActivated == True):
        responseDict['error'] = "The game has already started."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        if (len(GameStatus.playerList) == 4):
            responseDict['error'] = "The game is full."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            duplicateUser = False
            for player in GameStatus.playerList:
                if (player.socketId == request.sid):
                    duplicateUser = True
            if (duplicateUser):
                responseDict['error'] = "You are already in the game."
                response = json.dumps(responseDict)
                socketio.emit('game update', response, room = request.sid)
            else:
                playerName = datainput["user_name"]
                sys.stdout.write('Received: ' + playerName + '\n')
                sys.stdout.flush()
                socketId = request.sid
                createPlayer(playerName, socketId)
                for i in range(len(GameStatus.playerList)):
                    response = Serialize(GameStatus.playerList[i].playerId)
                    socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)

def LeaveGame(pid):
    sys.stdout.write("Player " + str(pid) + " has left. \n")
    sys.stdout.flush()
    #find player location in array
    for i in range(len(GameStatus.playerList)):
        if (GameStatus.playerList[i].playerId == pid):
            playerLocation = i  
    if (GameStatus.isGameActivated == False):
        #Remove player
        player = GameStatus.playerList[playerLocation]
        GameStatus.playerList.remove(player)
        #Update player IDs
        for i in range(len(GameStatus.playerList)):
            if (GameStatus.playerList[i].playerId > pid):
                GameStatus.playerList[i].playerId -= 1
        for i in range(len(GameStatus.playerList)):
            response = Serialize(GameStatus.playerList[i].playerId)
            socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)
    else:
        #Return their cards to the deck
        for i in range(len(GameStatus.playerList[playerLocation].hand)):
            GameStatus.table.Deck.append(GameStatus.playerList[playerLocation].hand.pop())
        #Check to see if it was their turn
        flag = False
        if (GameStatus.playerList[playerLocation].isTurn == True):
            flag = True
            endTurn(True)
        #Remove player - Move this to endTurn function?
        player = GameStatus.playerList[playerLocation]
        GameStatus.playerList.remove(player)
        GameStatus.currentPlayerId = GameStatus.playerList[GameStatus.currentPlayerIndex].playerId
        #Catch this special case
        if (flag):
            drawCard()
        else:
            if (GameStatus.currentPlayerIndex >= len(GameStatus.playerList)):
                GameStatus.currentPlayerIndex -= 1 
        #Update all players
        for i in range(len(GameStatus.playerList)):
            response = Serialize(GameStatus.playerList[i].playerId)
            socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)

@socketio.on('place card')
def PlaceCardInput(datainput, methods=['GET', 'POST']):
    responseDict = {}
    if (GameStatus.isGameActivated == False):
        responseDict['error'] = "The game has not started yet."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        if (GameStatus.playerList[GameStatus.currentPlayerIndex].socketId != request.sid):
            responseDict['error'] = "It is " + str(GameStatus.playerList[GameStatus.currentPlayerIndex].name) + "'s turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            if not("input_pile" in datainput):
                responseDict['error'] = "Select a pile."
                response = json.dumps(responseDict)
                socketio.emit('game update', response, room = request.sid)
            else:
                if (datainput["input_card"] == "No Card Selected"):
                    responseDict['error'] = "Select a card."
                    response = json.dumps(responseDict)
                    socketio.emit('game update', response, room = request.sid)
                else:
                    pile = datainput["input_pile"]
                    player = GameStatus.playerList[GameStatus.currentPlayerIndex]
                    cardPosition = 0
                    for thisCard in player.hand:
                        if thisCard.string == datainput["input_card"]:
                            cardPosition = thisCard.position
                            card = player.hand.pop(thisCard.position)
                    table = GameStatus.table
                    result = placeCard(player, card, pile, table)
                    if ("error" in result):
                        #add card back to player hand
                        player.hand.insert(cardPosition, card)
                        response = json.dumps(result)
                        socketio.emit('game update', response, room = player.socketId)
                    else:
                        #check if the player won
                        if (len(GameStatus.playerList[GameStatus.currentPlayerIndex].hand) == 0):
                            endGame()
                        else:
                            for i in range(len(GameStatus.playerList)):
                                response = Serialize(GameStatus.playerList[i].playerId)
                                socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)
            

@socketio.on('move pile')
def MovePileInput(datainput, methods=['GET', 'POST']):
    if (GameStatus.isGameActivated == False):
        responseDict = {}
        responseDict['error'] = "The game has not started yet."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        if (GameStatus.playerList[GameStatus.currentPlayerIndex].socketId != request.sid):
            responseDict = {}
            responseDict['error'] = "It is " + str(GameStatus.playerList[GameStatus.currentPlayerIndex].name) + "'s turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            player = GameStatus.playerList[GameStatus.currentPlayerIndex]
            startPile = datainput["start_pile"]
            endPile = datainput["end_pile"]
            sys.stdout.write(player.name + " is moving pile " + startPile + " to " + endPile + '\n')
            sys.stdout.flush()
            result = movePile(datainput["start_pile"], datainput["end_pile"])
            if ("error" in result):
                response = json.dumps(result)
                socketio.emit('game update', response, room = player.socketId)
            else:
                for i in range(len(GameStatus.playerList)):
                    response = Serialize(GameStatus.playerList[i].playerId)
                    socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)
    
@socketio.on('end turn')
def EndTurnInput(methods=['GET', 'POST']):
    if (GameStatus.isGameActivated == False):
        responseDict = {}
        responseDict['error'] = "The game has not started yet."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        if (request.sid != GameStatus.playerList[GameStatus.currentPlayerIndex].socketId):
            responseDict = {}
            responseDict['error'] = "It is not your turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            sys.stdout.write("PlayerId " + str(GameStatus.currentPlayerId) + " ended turn.\n")
            sys.stdout.flush()
            endTurn(False)
            for i in range(len(GameStatus.playerList)):
                response = Serialize(GameStatus.playerList[i].playerId)
                socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)

#Called when a user connects to the web page
@socketio.on('connection')
def NewConnection(json, methods=['GET', 'POST']):
    sys.stdout.write(json["data"] + '\n')
    sys.stdout.flush()

#Called when a user leaves the page
#Leaving the game on localhost will take a few seconds for the socket to disconnect, server will be immediate
@socketio.on('disconnect')
def RemoveConnection():
    sys.stdout.write(request.sid + ' disconnected. \n')
    sys.stdout.flush()
    #check if they were a player
    inGame = False
    for i in range(len(GameStatus.playerList)):
        if (GameStatus.playerList[i].socketId == request.sid):
            playerId = GameStatus.playerList[i].playerId
            inGame = True
    if (inGame == True):
        if (len(GameStatus.playerList) == 1 or len(GameStatus.playerList) == 2):
            endGameFromLackOfPlayers()
        else:
            LeaveGame(playerId)
    else:
        return
    
@app.route('/')
def sessions():
    return render_template('index.html')

#if python driver.py is called
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
