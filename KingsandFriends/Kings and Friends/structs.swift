//
//  createShuffledDeck.swift
//  Kings and Friends
//
//  Created by lundergust on 11/26/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import Foundation
import UIKit
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

struct TableImages {
    var tableSpot: String
    var imageString: String
}


extension UIImage{
//    func imageBlend(tableImages: [String]) -> String {
    func imageByCombiningImage(firstImage: UIImage, withImage secondImage: UIImage) -> UIImage {
        
        let newImageWidth  = max(firstImage.size.width,  secondImage.size.width )
        let newImageHeight = max(firstImage.size.height, secondImage.size.height)
        let newImageSize = CGSize(width : newImageWidth, height: newImageHeight)
        
        
        UIGraphicsBeginImageContextWithOptions(newImageSize, false, UIScreen.main.scale)
        
        let firstImageDrawX  = round((newImageSize.width  - firstImage.size.width  ) / 2)
        let firstImageDrawY  = round((newImageSize.height - firstImage.size.height ) / 2)
        
        let secondImageDrawX = round((newImageSize.width  - secondImage.size.width ) / 2)
        let secondImageDrawY = round((newImageSize.height - secondImage.size.height) / 2)
        
        firstImage.draw(at: CGPoint(x: firstImageDrawX,  y: firstImageDrawY))
        secondImage.draw(at: CGPoint(x: secondImageDrawX, y: secondImageDrawY))
        
        let image = UIGraphicsGetImageFromCurrentImageContext()
        
        UIGraphicsEndImageContext()
        
        
        return image!
    }
}

