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
        GameStatus.playerList[GameStatus.currentPlayer].isTurn = True
        GameStatus.table.N = [GameStatus.table.Deck.pop()]
        GameStatus.table.W = [GameStatus.table.Deck.pop()]
        GameStatus.table.E = [GameStatus.table.Deck.pop()]
        GameStatus.table.S = [GameStatus.table.Deck.pop()]
        distributeCards(GameStatus.playerList, GameStatus.table.Deck)
        drawCard(GameStatus.currentPlayer)
        sys.stdout.write("It is %s's turn" % GameStatus.playerList[GameStatus.currentPlayer].name + '\n')
        sys.stdout.flush()


def distributeCards(playerArray, deck):
    # Distributes 7 cards to each player
    for player in playerArray:
        i = 0
        while i < 1:
            thisCard = deck.pop()
            thisCard.position = i
            player.hand.append(thisCard)
            i += 1

def updateCardPositions(playerId):
    for i in range(len(GameStatus.playerList[playerId].hand)):
        GameStatus.playerList[playerId].hand[i].position = i
        

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
                updateCardPositions(player.playerId)
        elif (table.NW[-1].color != card.color):
            if (card.value == table.NW[-1].value - 1):
                table.NW.append(card)
                updateCardPositions(player.playerId)
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "N":
        if (not table.N):
            table.N.append(card)
            updateCardPositions(player.playerId)
        else:
            if (table.N[-1].color != card.color):
                if (card.value == table.N[-1].value - 1):
                    table.N.append(card)
                    updateCardPositions(player.playerId)
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
                updateCardPositions(player.playerId)
        elif (table.NE[-1].color != card.color):
            if (card.value == table.NE[-1].value - 1):
                table.NE.append(card)
                updateCardPositions(player.playerId)
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "W":
        if (not table.W):
            table.W.append(card)
            updateCardPositions(player.playerId)
        else:
            if (table.W[-1].color != card.color):
                if (card.value == table.W[-1].value - 1):
                    table.W.append(card)
                    updateCardPositions(player.playerId)
                else:
                    response["error"] = "Wrong number."
            else:
                response["error"] = "Wrong color."
    elif pile == "E":
        if (not table.E):
            table.E.append(card)
            updateCardPositions(player.playerId)
        else:
            if (table.E[-1].color != card.color):
                if (card.value == table.E[-1].value - 1):
                    table.E.append(card)
                    updateCardPositions(player.playerId)
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
                updateCardPositions(player.playerId)
        elif (table.SW[-1].color != card.color):
            if (card.value == table.SW[-1].value - 1):
                table.SW.append(card)
                updateCardPositions(player.playerId)
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    elif pile == "S":
        if (not table.S):
            table.S.append(card)
            updateCardPositions(player.playerId)
        else:
            if (table.S[-1].color != card.color):
                if (card.value == table.S[-1].value - 1):
                    table.S.append(card)
                    updateCardPositions(player.playerId)
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
                updateCardPositions(player.playerId)
        elif (table.SE[-1].color != card.color):
            if (card.value == table.SE[-1].value - 1):
                table.SE.append(card)
                updateCardPositions(player.playerId)
            else:
                response["error"] = "Wrong number."
        else:
            response["error"] = "Wrong color."
    return response

def drawCard(player):
    card = GameStatus.table.Deck.pop()
    card.position = len(GameStatus.playerList[player].hand)
    GameStatus.playerList[player].hand.append(card)

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

def endTurn():
    if (GameStatus.isGameActivated == False):
        return None
    GameStatus.playerList[GameStatus.currentPlayer].isTurn = False
    if GameStatus.currentPlayer == 3:
        GameStatus.currentPlayer = 0
        GameStatus.playerList[GameStatus.currentPlayer].isTurn = True
    else:
        GameStatus.currentPlayer += 1
        GameStatus.playerList[GameStatus.currentPlayer].isTurn = True
    #Draw card for next player
    drawCard(GameStatus.currentPlayer)

def endGame():
    responseDict = {}
    sys.stdout.write("The game is over. " + GameStatus.playerList[GameStatus.currentPlayer].name + " wins.\n")
    sys.stdout.flush()
    responseDict["winner"] = str(GameStatus.currentPlayer)
    GameStatus.currentPlayer = 0
    GameStatus.playerList[GameStatus.currentPlayer].isTurn = False
    for i in range(len(GameStatus.playerList)):
        GameStatus.playerList[i].hand = []
    GameStatus.table = Table(createDeck())
    for i in range(len(GameStatus.playerList)):
        response = json.dumps(responseDict)
        socketio.emit('game over', response, room = GameStatus.playerList[i].socketId)

#WebAPI
url = 'http://localhost:5000'
app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('join game')
def JoinGame(datainput, methods=['GET', 'POST']):
    if (len(GameStatus.playerList) == 4):
        responseDict = {}
        responseDict['error'] = "The game is full."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        duplicateUser = False
        for player in GameStatus.playerList:
            if (player.socketId == request.sid):
                duplicateUser = True
        if (duplicateUser):
            responseDict = {}
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

@app.route('/GetStatus', methods=['GET'])
def GetStatus():
    return Serialize()

@socketio.on('place card')
def PlaceCardInput(datainput, methods=['GET', 'POST']):
    if (GameStatus.isGameActivated == False):
        responseDict = {}
        responseDict['error'] = "The game has not started yet."
        response = json.dumps(responseDict)
        socketio.emit('game update', response, room = request.sid)
    else:
        if (GameStatus.playerList[GameStatus.currentPlayer].socketId != request.sid):
            responseDict = {}
            responseDict['error'] = "It is " + str(GameStatus.playerList[GameStatus.currentPlayer].name) + "'s turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            pile = datainput["input_pile"]
            player = GameStatus.playerList[GameStatus.currentPlayer]
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
                if (len(GameStatus.playerList[GameStatus.currentPlayer].hand) == 0):
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
        if (GameStatus.playerList[GameStatus.currentPlayer].socketId != request.sid):
            responseDict = {}
            responseDict['error'] = "It is " + str(GameStatus.playerList[GameStatus.currentPlayer].name) + "'s turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            player = GameStatus.playerList[GameStatus.currentPlayer]
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
        if (request.sid != GameStatus.playerList[GameStatus.currentPlayer].socketId):
            responseDict = {}
            responseDict['error'] = "It is not your turn."
            response = json.dumps(responseDict)
            socketio.emit('game update', response, room = request.sid)
        else:
            endTurn()
            sys.stdout.write("PlayerId " + str(GameStatus.currentPlayer) + " ended turn.\n")
            sys.stdout.flush()
            for i in range(len(GameStatus.playerList)):
                response = Serialize(GameStatus.playerList[i].playerId)
                socketio.emit('game update', response, room = GameStatus.playerList[i].socketId)

#Called when a user connects to the web page
@socketio.on('new connection')
def NewConnection(json, methods=['GET', 'POST']):
    sys.stdout.write(json["data"] + '\n')
    sys.stdout.flush()
    
@app.route('/')
def sessions():
    return render_template('index.html')

#if python driver.py is called
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
