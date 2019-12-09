def PlayerTurn(turn_player,table,GameStatus):
    EndTurn = False
    print(turn_player.name + " it's your turn!")
    while EndTurn == False:
        print("Table:")
        print(table.NW[-1]+'-'+table.NW[0]+"    "+table.N[-1]+'-'+table.N[0]+"    "+table.NE[-1]+'-'+table.NE[0]+"\n"
                table.W[-1]+'-'+table.W[0]+"    "+"D"+"    "+table.E[-1]+'-'+table.E[0]+"\n"
                table.SW[-1]+'-'+table.SW[0]+"    "+table.S[-1]+'-'+table.S[0]+"    "+table.SE[-1]+'-'+table.SE[0])
        print("Hand:")
        print("Cards : ",i+" " for i in turn_player.hand)
        selection = input("Select card: ")
