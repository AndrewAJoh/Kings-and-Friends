//
//  shuffleDeck.swift
//  Kings and Friends
//
//  Created by lundergust on 11/26/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import Foundation
// [Hearts:1, Diamonds:2, Clubs:3, Spades:4]
func shuffleDeck() -> [Card] {
    var shuffledDeck = [Card]()
    // Create Hearts
    let aceHearts = Card(value: 1, suit: 1, image: "AH.png") // Ace
    let twoHearts = Card.init(value: 2, suit: 1, image: "2H.png")
    let threeHearts = Card.init(value: 3, suit: 1, image: "3H.png")
    let fourHearts = Card.init(value: 4, suit: 1, image: "4H.png")
    let fiveHearts = Card.init(value: 5, suit: 1, image: "5H.png")
    let sixHearts = Card.init(value: 6, suit: 1, image: "6H.png")
    let sevenHearts = Card.init(value: 7, suit: 1, image: "7H.png")
    let eightHearts = Card.init(value: 8, suit: 1, image: "8H.png")
    let nineHearts = Card.init(value: 9, suit: 1, image: "9H.png")
    let tenHearts = Card.init(value: 10, suit: 1, image: "10H.png")
    let jackHearts = Card.init(value: 11, suit: 1, image: "JH.png") //Jack
    let queenHearts = Card.init(value: 12, suit: 1, image: "QH.png") // Queen
    let kingHearts = Card.init(value: 13, suit: 1, image: "KH.png") // King
    
    
    // Create Diamonds
    let aceDiamonds = Card.init(value: 1, suit: 2, image: "AD.png") // Ace
    let twoDiamonds = Card.init(value: 2, suit: 2, image: "2D.png")
    let threeDiamonds = Card.init(value: 3, suit: 2, image: "3D.png")
    let fourDiamonds = Card.init(value: 4, suit: 2, image: "4d.png")
    let fiveDiamonds = Card.init(value: 5, suit: 2, image: "5D.png")
    let sixDiamonds = Card.init(value: 6, suit: 2, image: "6D.png")
    let sevenDiamonds = Card.init(value: 7, suit: 2, image: "7D.png")
    let eightDiamonds = Card.init(value: 8, suit: 2, image: "8D.png")
    let nineDiamonds = Card.init(value: 9, suit: 2, image: "9D.png")
    let tenDiamonds = Card.init(value: 10, suit: 2, image: "10D.png")
    let jackDiamonds = Card.init(value: 11, suit: 2, image: "JD.png") //Jack
    let queenDiamonds = Card.init(value: 12, suit: 2, image: "QD.png") // Queen
    let kingDiamonds = Card.init(value: 13, suit: 2, image: "KD.png") // King
    
    // Create Clubs
    let aceClubs = Card.init(value: 1, suit: 3, image: "AC.png") // Ace
    let twoClubs = Card.init(value: 2, suit: 3, image: "2C.png")
    let threeClubs = Card.init(value: 3, suit: 3, image: "3C.png")
    let fourClubs = Card.init(value: 4, suit: 3, image: "4C.png")
    let fiveClubs = Card.init(value: 5, suit: 3, image: "5C.png")
    let sixClubs = Card.init(value: 6, suit: 3, image: "6C.png")
    let sevenClubs = Card.init(value: 7, suit: 3, image: "7C.png")
    let eightClubs = Card.init(value: 8, suit: 3, image: "8C.png")
    let nineClubs = Card.init(value: 9, suit: 3, image: "9C.png")
    let tenClubs = Card.init(value: 10, suit: 3, image: "10C.png")
    let jackClubs = Card.init(value: 11, suit: 3, image: "11C.png") //Jack
    let queenClubs = Card.init(value: 12, suit: 3, image: "12C.png") // Queen
    let kingClubs = Card.init(value: 13, suit: 3, image: "13C.png") // King
    
    // Create Spades
    let aceSpades = Card.init(value: 1, suit: 4, image: "1S.png") // Ace
    let twoSpades = Card.init(value: 2, suit: 4, image: "2S.png")
    let threeSpades = Card.init(value: 3, suit: 4, image: "3S.png")
    let fourSpades = Card.init(value: 4, suit: 4, image: "4S.png")
    let fiveSpades = Card.init(value: 5, suit: 4, image: "5S.png")
    let sixSpades =  Card.init(value: 6, suit: 4, image: "6S.png")
    let sevenSpades = Card.init(value: 7, suit: 4, image: "7S.png")
    let eightSpades = Card.init(value: 8, suit: 4, image: "8S.png")
    let nineSpades = Card.init(value: 9, suit: 4, image: "9S.png")
    let tenSpades = Card.init(value: 10, suit: 4, image: "10S.png")
    let jackSpades = Card.init(value: 11, suit: 4, image: "11S.png") //Jack
    let queenSpades = Card.init(value: 12, suit: 4, image: "12S.png") // Queen
    let kingSpades = Card.init(value: 13, suit: 4, image: "13S.png") // King
    
    shuffledDeck = [aceHearts,twoHearts,threeHearts,fourHearts,fiveHearts,sixHearts,sevenHearts,eightHearts,nineHearts,tenHearts,jackHearts,queenHearts,kingHearts,aceDiamonds,twoDiamonds,threeDiamonds,fourDiamonds,fiveDiamonds,sixDiamonds,sevenDiamonds,eightDiamonds,nineDiamonds,tenDiamonds,jackDiamonds,queenDiamonds,kingDiamonds,aceClubs,twoClubs,threeClubs,fourClubs,fiveClubs,sixClubs,sevenClubs,eightClubs,nineClubs,tenClubs,jackClubs,queenClubs,kingClubs,aceSpades,twoSpades,threeSpades,fourSpades,fiveSpades,sixSpades,sevenSpades,eightSpades,nineSpades,tenSpades,jackSpades,queenSpades,kingSpades]
    shuffledDeck = shuffledDeck.shuffled()
    return shuffledDeck
    }
