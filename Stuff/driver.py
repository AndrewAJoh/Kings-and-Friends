from player import Player
from card import Card
import random


def driver():
    p1 = Player(input("Enter Name: "))
    p2 = Player(input("Enter Name: "))
    p3 = Player(input("Enter Name: "))
    p4 = Player(input("Enter Name: "))
    playerArray = [p1, p2, p3, p4]
    deck = createDeck()
    distributeCards(playerArray, deck)
    table = populateTable(deck)

    print(p1.name + " has joined the table!")
    print("Is turn? %s" % p1.isTurn)
    print("%s has these cards: " % p1.name)
    p1HandString = ""
    for card in p1.hand:
        p1HandString = p1HandString + str(card.value) + str(card.suit) + ", "
    print(p1HandString[:-2])

    print(p2.name + " has joined the table!")
    print("Is turn? %s" % p2.isTurn)
    print("%s has these cards: " % p2.name)
    p2HandString = ""
    for card in p2.hand:
        p2HandString = p2HandString + str(card.value) + str(card.suit) + ", "
    print(p2HandString[:-2])

    print(p3.name + " has joined the table!")
    print("Is turn? %s" % p3.isTurn)
    print("%s has these cards: " % p3.name)
    p3HandString = ""
    for card in p3.hand:
        p3HandString = p3HandString + str(card.value) + str(card.suit) + ", "
    print(p3HandString[:-2])

    print(p4.name + " has joined the table!")
    print("Is turn? %s" % p4.isTurn)
    print("%s has these cards: " % p4.name)
    p4HandString = ""
    for card in p4.hand:
        p4HandString = p4HandString + str(card.value) + str(card.suit) + ", "
    print(p4HandString[:-2])


def distributeCards(playerArray, deck):
    # Distributes 7 cards to each player
    for player in playerArray:
        i = 0
        while i < 7:
            player.hand.append(deck.pop())
            i += 1


def createDeck():
    # Creates and shuffles 52-card deck
    deck = []
    for i in range(13):
        deck.append(Card(i + 1, "H"))
        deck.append(Card(i + 1, "D"))
        deck.append(Card(i + 1, "C"))
        deck.append(Card(i + 1, "S"))
        random.shuffle(deck)
    return deck


def populateTable(deck):
    # Populates 3x3 array with 4 starter cards at N, S, E, W, and the deck in the center
    table = [[[], [], []], [[], [], []], [[], [], []]]
    north = table[2][1]
    northeast = table[2][2]
    east = table[1][2]
    southeast = table[0][2]
    south = table[0][1]
    southwest = table[0][0]
    west = table[1][0]
    northwest = table[2][0]
    center = table[1][1]

    north.append(deck.pop())
    south.append(deck.pop())
    east.append(deck.pop())
    west.append(deck.pop())
    middle = deck
    return table


if __name__ == "__main__":
    driver()
