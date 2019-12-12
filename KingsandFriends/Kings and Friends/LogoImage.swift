//
//  LogoImage.swift
//  Kings and Friends
//
//  Created by lundergust on 11/25/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import SwiftUI

struct LogoImage: View {
    var body: some View {
        Image("Untitled drawing")
        .background(Color.init(red: 0.13, green: 0.55, blue: 0.13))
        .clipShape(Circle())
        .overlay(
            Circle().stroke(Color.gray, lineWidth: 8))
//            .shadow(radius:10)
            .padding(.all, 200)
    }
}

struct LogoImage_Previews: PreviewProvider {
    static var previews: some View {
        LogoImage()
    }
}
