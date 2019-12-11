from player import Player
from card import Card
from table import Table
import random
from flask import request, Flask, jsonify
import json
import sys
from gamestatus import GameStatus, Serialize


def driver():
    isGameActivated = True
    p1 = GameStatus.playerList[0]
    p2 = GameStatus.playerList[1]
    p3 = GameStatus.playerList[2]
    p4 = GameStatus.playerList[3]
    playerArray = [p1, p2, p3, p4]
    deck = createDeck()
    distributeCards(playerArray, deck)
    table = Table(deck)
    # random.shuffle(playerArray)
    currentPlayer = playerArray[0]
    currentPlayer.isTurn = True
    while isGameActivated == True:
        printTable(table)
        # draw card
        currentPlayer = checkIfTurn(playerArray)
        drawCard(currentPlayer, table)
        print("It is %s's turn" % currentPlayer.name)
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
    player = Player(playerName)
    GameStatus.playerList.append(player)
    if (len(GameStatus.playerList) == 4):
        sys.stdout.write("The game will now start")
        driver()


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


def distributeCards(playerArray, deck):
    # Distributes 7 cards to each player
    for player in playerArray:
        i = 0
        while i < 7:
            thisCard = deck.pop()
            thisCard.position = i
            player.hand.append(thisCard)
            i += 1


def placeCard(player, card, pile, table):
    # Takes input card from current player through button action, places card in desired pile.
    # Card will be a card object containing value, suit, and location in player hand list
    # Must contain logic for alternating black/red as well as being 1 value lower than previous
    if pile == "NW":
        if table.NW[-1].color != card.color:
            if card.value == table.NW[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.NW.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "N":
        if table.N[-1].color != card.color:
            if card.value == table.N[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.N.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "NE":
        if table.NE[-1].color != card.color:
            if card.value == table.NE[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.NE.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "W":
        if table.W[-1].color != card.color:
            if card.value == table.W[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.W.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "E":
        if table.E[-1].color != card.color:
            if card.value == table.E[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.E.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SW":
        if table.SW[-1].color != card.color:
            if card.value == table.SW[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.SW.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "S":
        if table.S[-1].color != card.color:
            if card.value == table.S[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.S.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SE":
        if table.SE[-1].color != card.color:
            if card.value == table.SE[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.SE.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")


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


def drawCard(player, table):
    thisCard = table.Deck.pop()
    player.hand.append(thisCard)


def addPlayer(playerArray):
    playerArray.append(Player(input("Enter Name: ")))
    return playerArray


def movePile(pile, destination, table):
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


def endTurn(playerArray, currentPlayer):
    index = playerArray.index(currentPlayer)
    currentPlayer.isTurn = False
    if index == 3:
        newIndex = 0
        playerArray[newIndex].isTurn = True
    else:
        playerArray[index + 1].isTurn = True


def checkIfTurn(playerArray):
    for player in playerArray:
        if player.isTurn == True:
            currentPlayer = player
            return currentPlayer


# WebAPI
url = 'https://localhost:5000'
app = Flask(__name__)


@app.route('/JoinGame', methods=['POST'])
def JoinGame():
    playerName = request.get_json()
    sys.stdout.write('Received: ' + playerName)
    createPlayer(playerName)
    sys.stdout.write('There are now ' +
                     str(len(GameStatus.playerList)) + ' players in the game')
    result = Serialize()
    return result


# if python driver.py is called
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000, ssl_context='adhoc')
