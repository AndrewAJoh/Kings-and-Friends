////
////  driver.swift
////  Kings and Friends
////
////  Created by lundergust on 12/10/19.
////  Copyright © 2019 lundergust. All rights reserved.
////

import Foundation
import UIKit

func driver() -> ([Player], [Card], Table, [[String]]) {
    var isGameActivated = true
    var p1 = Player(name: "Joe", hand: [], isTurn: true)
    var p2 = Player(name: "Austin", hand: [], isTurn: false)
    var p3 = Player(name: "Derek", hand: [], isTurn: false)
    var p4 = Player(name: "Andy", hand: [], isTurn: false)
    var playerArray = [p1, p2, p3, p4]
    var deck = createDeck()
    distributeCards(playerArray: &playerArray, deck: &deck)
    var table = createTable(deck: &deck)
    var currentPlayer = playerArray[0]
    currentPlayer.isTurn = true
    var imageStrings = updateTableImages(table: &table, deck: &deck, playerArray: &playerArray)
    return (playerArray, deck, table, imageStrings)
}


func createDeck() -> [Card] {
    var deck = [Card]()
    for i in 0..<14 {
        deck.append(Card(value: i + 1, suit: "H", color: "R", image: String(i+1) + "H.png", string: String(i+1) + "H", position: 0))
        deck.append(Card(value: i + 1, suit: "D", color: "R", image: String(i+1) + "D.png", string: String(i+1) + "D", position: 0))
        deck.append(Card(value: i + 1, suit: "C", color: "B", image: String(i+1) + "C.png", string: String(i+1) + "C", position: 0))
        deck.append(Card(value: i + 1, suit: "S", color: "B", image: String(i+1) + "S.png", string: String(i+1) + "S", position: 0))
    }
    return deck
}

func distributeCards(playerArray: inout [Player], deck: inout [Card]) {
    for i in 0..<playerArray.count {
        var j = 0
        while j < 7 {
            var thisCard: Card = deck.popLast()!
            thisCard.position = j
            playerArray[i].hand.append(thisCard)
            j+=1
        }
    }
}

func createTable(deck: inout [Card]) -> Table {
    var table = Table(NW: [], N: [deck.popLast()!], NE: [], W: [deck.popLast()!], E: [deck.popLast()!], SW: [], S: [deck.popLast()!], SE: [], Deck: deck)
    return table
}

func updateTableImages(table: inout Table, deck: inout [Card], playerArray: inout [Player]) -> [[String]] {
    var imageStringsggs: [(String, [String])]
    var imageStrings = [[String]]()
//    NW
    for card in table.NW {
        var NWimages = [String]()
        NWimages.append(card.image)
        imageStrings.append(NWimages)
    }
//    N
    for card in table.N {
        var Nimages = [String]()
        Nimages.append(card.image)
        imageStrings.append(Nimages)    }
//    NE
    for card in table.NE {
        var NEimages = [String]()
        NEimages.append(card.image)
        imageStrings.append(NEimages)    }
//    W
    for card in table.W {
        var Wimages = [String]()
        Wimages.append(card.image)
        imageStrings.append(Wimages)    }
//    E
    for card in table.E {
        var Eimages = [String]()
        Eimages.append(card.image)
        imageStrings.append(Eimages)    }
//    SW
    for card in table.SW {
        var SWimages = [String]()
        SWimages.append(card.image)
        imageStrings.append(SWimages)    }
//    S
    for card in table.S {
        var Simages = [String]()
        Simages.append(card.image)
        imageStrings.append(Simages)    }
//    SE
    for card in table.SE {
        var SEimages = [String]()
        SEimages.append(card.image)
        imageStrings.append(SEimages)    }
    return imageStrings
}
