//
//  ContentView.swift
//  Kings and Friends
//
//  Created by lundergust on 11/24/19.
//  Copyright © 2019 lundergust. All rights reserved.
//

import SwiftUI


struct ContentView: View {
    var (playerArray, deck, table, imageStrings) = driver()
//    NW

    var body: some View {
        ZStack {

            LogoImage()
                .padding(.top, 60)
            .background(Color.init(red: 0.13, green: 0.4, blue: 0.13))
            .edgesIgnoringSafeArea(.all)
            VStack {
    //            North Piles
                HStack {
    //                NorthWest
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {

                        Image(imageStrings[0][0])
                        .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                    Spacer()

    //                North
                    ZStack {
                        Button(action: {}) {
                            Image(imageStrings[1][0])
                            .resizable()
                                .frame(width:71.4, height:100.0)
                        }
                        Button(action: {}) {
                            Image("6D")
                            .resizable()
                                .frame(width:71.4, height:100.0)
                                .offset(y:-30)
                        }
                    }
                    Spacer()

    //                NorthEast
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[2][0])
                        .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                }
                .frame(width: 330.0)

                Spacer()

                
    //        Middle plane piles
                HStack {
    //                West
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[3][0])
                            .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                    Spacer()
    //                Deck
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image("cardDeck")
                            .resizable()
                            .frame(width:85.68, height:120.0)
                    }
                    Spacer()
    //                East
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[4][0])
                            .resizable()
                            .frame(width:71.4, height:100.0)
                     }
                }
                .frame(width: 330.0)
                
                Spacer()

                
    //          South Piles
                HStack {
    //                South West
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[5][0])
                        .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                    Spacer()

    //                South
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[6][0])
                            .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                    Spacer()

    //                South East
                    Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/) {
                        Image(imageStrings[7][0])
                            .resizable()
                            .frame(width:71.4, height:100.0)
                    }
                }
                .frame(width: 330.0)

            }
            .frame(width: nil, height: 400.0)
                

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
