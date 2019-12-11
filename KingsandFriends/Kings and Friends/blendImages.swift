//
//  blendImages.swift
//  Kings and Friends
//
//  Created by lundergust on 12/10/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import Foundation
func blendImages() {


    let renderer = UIGraphicsImageRenderer(size: CGSize(width:  1000, height: 833))

    let img = renderer.image { ctx in



        let bgImage = currentImage
        bgImage?.draw(at: CGPoint(x: 0, y: 0))


        let frame = UIImage(named: "Hasscience")
        frame?.draw(at: CGPoint(x: 0, y: 0))


    }


    imageView.image = img

}
