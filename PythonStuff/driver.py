from player import Player
from card import Card
from table import Table
import random
from flask import request, Flask, jsonify
import json
import sys
from gamestatus import GameStatus, Serialize

def driver():
    table = GameStatus.table
    return None
    printTable(table)
    # While isGameActivated = true
    currentPlayer = checkIfTurn(playerArray)
    drawCard(currentPlayer, table)
    currentHand = ""
    for item in currentPlayer.hand:
        currentHand = currentHand + item.string + ", "
    print("Your hand: %s" % currentHand[:-2])
    command = input(
        "Do you want to placeCard() , movePile() , or endTurn() ?")
    if command == "placeCard()":
        print("Your cards are: %s" % currentHand)
        card = input("What card would you like to move?")
        for thisCard in currentPlayer.hand:
            if thisCard.string == card:
                card = currentPlayer.hand.pop(thisCard.position)
        pile = input(
            "What pile would you like to place it on? (N, SW, E, etc.)")
        placeCard(currentPlayer, card, pile, table)
    elif command == "movePile()":
        pile = input("What pile would you like to move?")
        destination = input("Where would you like to place this pile?")
        movePile(pile, destination, table)
    elif command == "endTurn()":
        endTurn(playerArray, currentPlayer)
    
        
def createPlayer(playerName):
    playerId = len(GameStatus.playerList)
    player = Player(playerName, playerId)
    GameStatus.playerList.append(player)
    sys.stdout.write('There are now ' + str(len(GameStatus.playerList)) + ' players in the game' + '\n')
    sys.stdout.flush()
    if (len(GameStatus.playerList) == 4):
        startGame()
        driver()

def startGame():
        sys.stdout.write("The game will now start\n")
        sys.stdout.flush()
        GameStatus.isGameActivated = True
        GameStatus.playerList[GameStatus.currentPlayer].isTurn = True
        distributeCards(GameStatus.playerList, GameStatus.table.Deck)
        drawCard(GameStatus.currentPlayer)
        sys.stdout.write("It is %s's turn" % GameStatus.playerList[GameStatus.currentPlayer].name + '\n')
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

def updateCardPositions(playerId):
    for i in range(len(GameStatus.playerList[playerId].hand)):
        if (GameStatus.playerList[playerId].hand[i].position != i):
            GameStatus.playerList[playerId].hand[i].position = i
        

def placeCard(player, card, pile, table):
    # Takes input card from current player through button action, places card in desired pile.
    # Card will be a card object containing value, suit, and location in player hand list
    # Must contain logic for alternating black/red as well as being 1 value lower than previous
    if (GameStatus.isGameActivated == False):
        return None
    if pile == "NW":
        if (not table.NW):
            if (card.value != 13):
                return "You must place a King in the corner first"
            else:
                table.NW.append(card)
                updateCardPositions(player.playerId)
        elif (table.NW[-1].color != card.color):
            if (card.value == table.NW[-1].value - 1):
                table.NW.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "N":
        if (table.N[-1].color != card.color):
            if (card.value == table.N[-1].value - 1):
                table.N.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "NE":
        if (not table.NE):
            if (card.value != 13):
                return "You must place a King in the corner first"
            else:
                table.NE.append(card)
                updateCardPositions(player.playerId)
        elif (table.NE[-1].color != card.color):
            if (card.value == table.NE[-1].value - 1):
                table.NE.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "W":
        if (table.W[-1].color != card.color):
            if (card.value == table.W[-1].value - 1):
                table.W.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "E":
        if (table.E[-1].color != card.color):
            if (card.value == table.E[-1].value - 1):
                table.E.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SW":
        if (not table.SW):
            if (card.value != 13):
                return "You must place a King in the corner first"
            else:
                table.SW.append(card)
                updateCardPositions(player.playerId)
        elif (table.SW[-1].color != card.color):
            if (card.value == table.SW[-1].value - 1):
                table.SW.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "S":
        if (table.S[-1].color != card.color):
            if (card.value == table.S[-1].value - 1):
                table.S.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SE":
        if (not table.SE):
            if (card.value != 13):
                return "You must place a King in the corner first"
            else:
                table.SE.append(card)
                updateCardPositions(player.playerId)
        elif (table.SE[-1].color != card.color):
            if (card.value == table.SE[-1].value - 1):
                table.SE.append(card)
                updateCardPositions(player.playerId)
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")
    return Serialize()


def printTable(table):
    nw = ""
    n = ""
    ne = ""
    w = ""
    d = ""
    e = ""
    sw = ""
    s = ""
    se = ""
    if len(table.NW) != 0:
        for item in table.NW:
            nw = nw + str(item.value) + str(item.suit) + ", "
    if len(table.N) != 0:
        for item in table.N:
            n = n + str(item.value) + str(item.suit) + ", "
    if len(table.NE) != 0:
        for item in table.NE:
            ne = ne + str(item.value) + str(item.suit) + ", "
    if len(table.W) != 0:
        for item in table.W:
            w = w + str(item.value) + str(item.suit) + ", "
    if len(table.E) != 0:
        for item in table.E:
            e = e + str(item.value) + str(item.suit) + ", "
    if len(table.SW) != 0:
        for item in table.SW:
            sw = sw + str(item.value) + str(item.suit) + ", "
    if len(table.S) != 0:
        for item in table.S:
            s = s + str(item.value) + str(item.suit) + ", "
    if len(table.SE) != 0:
        for item in table.SE:
            se = se + str(item.value) + str(item.suit) + ", "

    print("|  {0}  |  {1}  |  {2}  |".format(
        nw, n, ne))
    print("|  {0}  |    |  {1}  |".format(
        w, e))
    print("|  {0}  |  {1}  |  {2}  |".format(
        sw, s, se))
    print("")


def drawCard(player):
    card = GameStatus.table.Deck.pop()
    card.position = len(GameStatus.playerList[player].hand)
    GameStatus.playerList[player].hand.append(card)
    

def addPlayer(playerArray):
    playerArray.append(Player(input("Enter Name: ")))
    return playerArray


def movePile(pile, destination, table):
    if (GameStatus.isGameActivated == False):
        return None
    # check if there are cards in destination pile
    if len(getattr(table, destination)) != 0:
        # check for opposite color rule
        if getattr(table, destination)[-1].color != getattr(table, pile)[0].color:
            # check for sequence rule
            if getattr(table, pile)[0].value == getattr(table, destination)[-1].value - 1:
                # iterate through pile loop and remove cards, placing in destination list
                for card in getattr(table, pile):
                    getattr(table, destination).append(
                        getattr(table, pile).pop(card))
            else:
                print(
                    "Highest card is not one less than the last card in destination pile")
        else:
            print(
                "Highest card is not of opposite color to the last card in destination pile")
    else:
        # if there are no cards in destination, only kings can be put in corner
        if destination == "NW" or destination == "NE" or destination == "SW" or destination == "SE":
            # check if highest card is king
            if getattr(table, pile)[0].value == 13:
                while len(getattr(table, pile)) > 0:
                    getattr(table, destination).append(
                        getattr(table, pile).pop(0))
            else:
                print("Only kings can start in the corner")
        else:
            # if not going in corner, can place any card
            while len(getattr(table, pile)) > 0:
                getattr(table, destination).append(
                    getattr(table, pile).pop(0))


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
    return Serialize()

def checkIfTurn(playerArray):
    for player in playerArray:
        if player.isTurn == True:
            currentPlayer = player
            return currentPlayer

#WebAPI
url = 'https://localhost:5000'
app = Flask(__name__)

@app.route('/JoinGame', methods=['POST'])
def JoinGame():
    if (len(GameStatus.playerList) == 4):
        return "The game is full"
    playerName = request.get_json()
    sys.stdout.write('Received: ' + playerName + '\n')
    sys.stdout.flush()
    createPlayer(playerName)
    result = Serialize()
    return result

@app.route('/GetStatus', methods=['GET'])
def GetStatus():
    result = Serialize()
    return result

@app.route('/PlaceCard', methods=['POST'])
def PlaceCardInput():
    requestInput = request.get_json()
    if (GameStatus.currentPlayer != requestInput[0]):
        return "It is not your turn. It is player " + str(GameStatus.playerList[GameStatus.currentPlayer].playerId) + "'s turn"
    playerFound = False
    for i in range(4):
        if GameStatus.playerList[i].playerId == requestInput[0]:
            playerFound = True
            player = GameStatus.playerList[i]
    if (playerFound == False):
        return "No player found with ID " + str(requestInput[0])
    cardFound = False
    for thisCard in player.hand:
        if thisCard.string == requestInput[1]:
            cardFound = True
            card = player.hand.pop(thisCard.position)
    if (cardFound == False):
        return "No card found for player " + player.name
    pile = requestInput[2]
    table = GameStatus.table
    sys.stdout.write("Now moving " + player.name + "'s " + card.string + " card to " + pile + '\n')
    sys.stdout.flush()
    return placeCard(player, card, pile, table)

@app.route('/EndTurn', methods=['POST'])
def EndTurnInput():
    requestInput = request.get_json()
    if (GameStatus.currentPlayer != requestInput):
        return "It is not your turn. It is player " + str(GameStatus.playerList[GameStatus.currentPlayer].playerId) + "'s turn"
    return endTurn()
    

#if python driver.py is called
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000, ssl_context='adhoc')
