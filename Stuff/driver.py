from player import Player
from card import Card
import random


def driver():
#Setting up players at table
    playerArray = []
    while len(playerArray) < 4:
        player = Player(str(input("Player Name: ")))
        playerArray.append(player)
#Dealing
    deck = createDeck()
    distributeCards(playerArray, deck)
    table = Table(deck)
    rand = random.randint(0,3)
    turn_player = playerArray[rand]
    turn_player.isTurn = True
    GameStatus = True

#Playing
    while GameStatus == True:
        PlayerTurn(turn_player,table,GameStatus)

def createDeck():
    # Creates and shuffles 52-card deck
    deck = []
    for i in range(14):
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
    if table.pile[-1].color != card.color:
        if card.value == table.pile[-1].value - 1:
            thisCard = player.hand.pop(card.position)
            table.pile.append(thisCard)


if __name__ == "__main__":
    driver()
