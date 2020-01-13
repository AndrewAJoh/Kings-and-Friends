//
//  SocketIOManager.swift
//  Kings and Friends
//
//  Created by lundergust on 1/12/20.
//  Copyright © 2020 lundergust. All rights reserved.
//

import UIKit


class SocketIOManager: NSObject {
    static let sharedInstance = SocketIOManager()
    
    override init() {
        super.init()
        let manager = SocketManager(socketURL: URL(string: "http://3.15.183.196/:5000")!, config: [.log(true), .compress])
           let socket = manager.defaultSocket

           socket.on(clientEvent: .connect) {data, ack in
               print("socket connected")
           }

           socket.on("currentAmount") {data, ack in
               guard let cur = data[0] as? Double else { return }
               
               socket.emitWithAck("canUpdate", cur).timingOut(after: 0) {data in
                   socket.emit("update", ["amount": cur + 2.50])
               }

               ack.with("Got your currentAmount", "dude")
           }

           socket.connect()
    }
    
}
