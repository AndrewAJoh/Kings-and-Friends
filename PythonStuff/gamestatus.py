import json

#GameStatus will have all relevant global objects we need for the lifetime of a game
class GameStatus:
    playerList = []
    

#Serialize will convert all global variables to json so it can be sent back
def Serialize():
    return json.dumps(GameStatus.playerList, default=lambda o: o.__dict__, indent=4)
