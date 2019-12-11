//
//  ContentView.swift
//  Kings and Friends
//
//  Created by lundergust on 11/24/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    @State private var showDetails = false

    var body: some View {
        ZStack() {
            Color.init(red: 0.13, green: 0.4, blue: 0.13).edgesIgnoringSafeArea(.all)
            LogoImage()
//                .offset(y: -100)
            
            // Draw Deck Button
            Button(action: {
                self.showDetails.toggle()
            }) {
                Image("cardDeck")
                .resizable()
                .frame(width: 100.0, height: 140.0)
            }
            if showDetails {
                Text("Follow the rules")
                    .font(.largeTitle)
            }
            
            // Initial Pile Buttons
            
            
            // Right
            HStack {
                Button(action: {
                    self.showDetails.toggle()
                }) {
                    Image("8H")
                    .resizable()
                        .frame(width: 71.4, height: 100.0)
                        .offset(x: 130.0)
                    Image("7C")
                    .resizable()
                        .frame(width: 71.4, height: 100)
                }
            }
            
            // Top
            VStack {
                Button(action: {
                       self.showDetails.toggle()
                   }) {
                       Image("11D")
                       .resizable()
                           .frame(width: 71.4, height: 100.0)
                           .offset(y: -160.0)
                }
            }
            
            // Left
            HStack {
                Button(action: {
                       self.showDetails.toggle()
                   }) {
                       Image("5S")
                       .resizable()
                           .frame(width: 71.4, height: 100.0)
                           .offset(x: -130.0)
                }
            }
            
            // Bottom
            VStack(spacing: 0.0) {
//                Spacer()
                Button(action: {
                       self.showDetails.toggle()
                   }) {
                       Image("7D")
                        
                        .resizable()
                           .frame(width: 71.4, height: 100.0)
                        Image("6C")
                        .resizable()
                            .frame(width: 71.4, height: 100)
//                            .offset(x: -80, y: 25)
                        Image("5D")
                        .resizable()
                            .frame(width: 71.4, height: 100)
//                            .offset(x: -160, y: 50)
                           
                }

            }
            .padding([.top], 0.0)
            .frame(width: 100.0, height: 800.0)
            .offset(x: 80, y: 160)
//            .position(x: CGFloat(480.0), y: CGFloat(569.0))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


func combineImages() {
    
}
