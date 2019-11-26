//
//  ContentView.swift
//  Kings and Friends
//
//  Created by lundergust on 11/24/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack(alignment: .leading) {
        Color.init(red: 0.13, green: 0.4, blue: 0.13).edgesIgnoringSafeArea(.all)
            LogoImage()
        }
    }
    

}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
