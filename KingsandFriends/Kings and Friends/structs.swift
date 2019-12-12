//
//  createShuffledDeck.swift
//  Kings and Friends
//
//  Created by lundergust on 11/26/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import Foundation
struct Card {
    var value: Int
    var suit: String
    var color: String
    var image: String
    var string: String
    var position: Int
}

struct Player {
    var name: String
    var hand: [Card]
    var isTurn: Bool
}

struct Table {
    var NW: [Card]
    var N: [Card]
    var NE: [Card]
    var W: [Card]
    var E: [Card]
    var SW: [Card]
    var S: [Card]
    var SE: [Card]
    var Deck: [Card]
}
