from player import Player
from card import Card
from table import Table
import random


def driver():
    isGameActivated = True
    while isGameActivated == True:

        p1 = Player(input("Enter Name: "))
        p2 = Player(input("Enter Name: "))
        p3 = Player(input("Enter Name: "))
        p4 = Player(input("Enter Name: "))
        playerArray = [p1, p2, p3, p4]
        deck = createDeck()
        distributeCards(playerArray, deck)
        table = Table(deck)

        print(p1.name + " has joined the table!")
        print("Is turn? %s" % p1.isTurn)
        print("%s has these cards: " % p1.name)
        p1HandString = ""
        for card in p1.hand:
            p1HandString = p1HandString + \
                str(card.value) + str(card.suit) + ", "
        print(p1HandString[:-2])

        print(p2.name + " has joined the table!")
        print("Is turn? %s" % p2.isTurn)
        print("%s has these cards: " % p2.name)
        p2HandString = ""
        for card in p2.hand:
            p2HandString = p2HandString + \
                str(card.value) + str(card.suit) + ", "
        print(p2HandString[:-2])

        print(p3.name + " has joined the table!")
        print("Is turn? %s" % p3.isTurn)
        print("%s has these cards: " % p3.name)
        p3HandString = ""
        for card in p3.hand:
            p3HandString = p3HandString + \
                str(card.value) + str(card.suit) + ", "
        print(p3HandString[:-2])

        print(p4.name + " has joined the table!")
        print("Is turn? %s" % p4.isTurn)
        print("%s has these cards: " % p4.name)
        p4HandString = ""
        for card in p4.hand:
            p4HandString = p4HandString + \
                str(card.value) + str(card.suit) + ", "
        print(p4HandString[:-2])

        random.shuffle(playerArray)
        currentPlayer = playerArray[0]
        currentPlayer.isTurn = True
        printTable(table)
        # draw card
        drawCard(currentPlayer, table)
        print("It is %s's turn" % playerArray[0].name)
        currentHand = ""
        for item in currentPlayer.hand:
            currentHand = currentHand + item.string + ", "
        print("Your hand: %s" % currentHand[:-2])

        command = input(
            "Do you want to placeCard() , movePile() , or endTurn() ?")
        if command == "placeCard()":
            print("Your cards are: %s" % currentHand)
            card = input("What card would you like to move?")
            for thisCard in p1.hand:
                if thisCard.string == card:
                    card = p1.hand.pop(thisCard.position)
            pile = input(
                "What pile would you like to place it on? (N, SW, E, etc.)")
            placeCard(currentPlayer, card, pile, table)


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
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "N":
        if table.N[-1].color != card.color:
            if card.value == table.N[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "NE":
        if table.NE[-1].color != card.color:
            if card.value == table.NE[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "W":
        if table.W[-1].color != card.color:
            if card.value == table.W[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "E":
        if table.E[-1].color != card.color:
            if card.value == table.E[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SW":
        if table.SW[-1].color != card.color:
            if card.value == table.SW[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "S":
        if table.S[-1].color != card.color:
            if card.value == table.S[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
            else:
                print("error")
        else:
            print("error")
    elif pile == "SE":
        if table.SE[-1].color != card.color:
            if card.value == table.SE[-1].value - 1:
                thisCard = player.hand.pop(card.position)
                table.pile.append(thisCard)
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


if __name__ == "__main__":
    driver()
