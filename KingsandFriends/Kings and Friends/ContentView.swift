//
//  ContentView.swift
//  Kings and Friends
//
//  Created by lundergust on 11/24/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import SwiftUI
import UIKit


//struct GroupView: View {
//    var body: some View {
//        VStack(alignment: .leading) {
//
//            Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
//                Image("6C")
//                .renderingMode(.original)
//                .resizable()
//                .frame(width:71.4, height:100.0)
//            }
//        }
//    }
//}





struct ContentView: View {
    var (playerArray, deck, table, NWimages, Nimages, NEimages, Wimages, Eimages, SWimages, Simages, SEimages) = driver()
    var displacement1 = -30
    var displacement2 = -30*2
    var displacement3 = -30*3
    var displacement4 = -30*4
    var displacement5 = -30*5
    var displacement6 = -30*6
    var displacement7 = -30*7
    var displacement8 = -30*8
    var displacement9 = -30*9
    var displacement10 = -30*10
    var displacement11 = -30*11
    var displacement12 = -30*12
    var displacement13 = -30*13
    var x = CGFloat(560)
    var y = CGFloat(420)
    var i = 0

    
    
    
    
    var body: some View {
        ZStack {
            
            LogoImage()
                .padding(.top, 60)
            .background(Color.init(red: 0.13, green: 0.4, blue: 0.13))
            .edgesIgnoringSafeArea(.all)
            
            NavigationView {
                    ScrollView(.horizontal) {
                        HStack() {
                            ForEach(0 ..< playerArray[0].hand.count) { pickle in
                                    VStack(alignment: .leading) {

                                Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
//                                    Image(self.playerArray[0].hand[self.i].image)
                                    Image("6D")
                                    .renderingMode(.original)
                                    .resizable()
                                    .frame(width:71.4, height:100.0)
                                }
                            }
                            }
                        }                        }.frame(height: 100)
                }
            .position(x: CGFloat(200), y: CGFloat(400))
            .frame(width: 400, height: 200)
            .background(Color.clear)
           
            
            ZStack {
            
    //            NW Pile
                ZStack {
                    if NWimages.count > 0 {
                        if NWimages[0] != "" {
                            Image(NWimages[0])
                            .renderingMode(.original)
                            .resizable()
                            .frame(width:71.4, height:100.0)
                            .position(x: 560, y: 430)
                        }
                    }
    //                ForEach(NWimages, id: \.self) { picture in
    //                    Image(picture)
    //                    .renderingMode(.original)
    //                    .resizable()
    //                    .frame(width:71.4, height:100.0)
    //                    .position(x: 560, y: 420)
    //                }
                    
                }.frame(width: 1360, height: 1180 )
                
    //            N Pile
                ZStack {
                   if Nimages.count > 0 {
                        if Nimages[0] != "" {
                            Image(String(Nimages[0]))
                            .renderingMode(.original)
                            .resizable()
                            .frame(width:71.4, height:100.0)
                            .position(x: 680, y: 430)
                        }
                    }
                }
                
    //            NE Pile
                ZStack {
                    if NEimages.count > 0 {
                         if NEimages[0] != "" {
                             Image(String(NEimages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 800, y: 430)
                         }
                     }
                }
                
    //            Deck
    //            West pile
                ZStack {
                    if Wimages.count > 0 {
                         if Wimages[0] != "" {
                             Image(String(Wimages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 560, y: 590)
                         }
                     }
                }
                
                    Image("cardDeck")
                        .renderingMode(.original)
                        .resizable()
                        .frame(width:85.68, height:120.0)
                        .position(x: 680, y: 590)
                
    //            E Pile
                ZStack {
                    if Eimages.count > 0 {
                         if Eimages[0] != "" {
                             Image(String(Eimages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 800, y: 590)
                         }
                     }
                }

                
    //            SW Pile
                ZStack {
                    if SWimages.count > 0 {
                         if SWimages[0] != "" {
                             Image(String(SWimages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 560, y: 750)
                         }
                     }
                }
                
                
    //            S Pile
                ZStack {
                    if Simages.count > 0 {
                         if Simages[0] != "" {
                             Image(String(Simages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 680, y: 750)
                         }
                     }
                }
                
    //            SE Pile
                ZStack {
                    if SEimages.count > 0 {
                         if SEimages[0] != "" {
                             Image(String(SEimages[0]))
                             .renderingMode(.original)
                             .resizable()
                             .frame(width:71.4, height:100.0)
                             .position(x: 800, y: 750)
                         }
                     }
                }
            }
            
        }
    }


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

//func addPlayer() -> Player {
//    let alert = UIAlertController(title: "Add Player", message: "Enter your name", preferredStyle: .alert)
//        alert.addTextField() { textField in
//        textField.placeholder = "Enter your name"
//    }
//    alert.addAction(UIAlertAction(title: "Cancel", style: .cancel) { _ in })
//    showAlert(alert: alert)
//    var newPlayer = Player(name:, name: <#String#>, hand: [], isTurn: false)
//    return newPlayer
//}

func showAlert(alert: UIAlertController) {
    if let controller = topMostViewController() {
        controller.present(alert, animated: true)
    }
}

private func keyWindow() -> UIWindow? {
    return UIApplication.shared.connectedScenes
        .filter {$0.activationState == .foregroundActive}
        .compactMap {$0 as? UIWindowScene}
        .first?.windows.filter {$0.isKeyWindow}.first
}

private func topMostViewController() -> UIViewController? {
    guard let rootController = keyWindow()?.rootViewController else {
        return nil
    }
    return topMostViewController(for: rootController)
}

private func topMostViewController(for controller: UIViewController) -> UIViewController {
    if let presentedController = controller.presentedViewController {
        return topMostViewController(for: presentedController)
    } else if let navigationController = controller as? UINavigationController {
        guard let topController = navigationController.topViewController else {
            return navigationController
        }
        return topMostViewController(for: topController)
    } else if let tabController = controller as? UITabBarController {
        guard let topController = tabController.selectedViewController else {
            return tabController
        }
        return topMostViewController(for: topController)
    }
    return controller
}




func combineImages() {
    
}

}
