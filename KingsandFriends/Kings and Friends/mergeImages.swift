//
//  mergeImages.swift
//  Kings and Friends
//
//  Created by lundergust on 11/27/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import Foundation
import SwiftUI
func mergeImages(a: String, b: String) {
    var image1 = Image(a)
    var image2 = Image(b)
    
    var size = CGSize(width: 300, height: 300)
    UIGraphicsBeginImageContext(size)

    let areaSize = CGRect(x: 0, y: 0, width: size.width, height: size.height)
    image1.draw(in: areaSize)

    image2.draw(in: areaSize, blendMode: .normal, alpha: 0.8)

    var newImage:UIImage = UIGraphicsGetImageFromCurrentImageContext()!
    UIGraphicsEndImageContext()
}

