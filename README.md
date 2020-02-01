# Kings-and-Friends
Kings and Friends is an implementation of the card game "Kings Corners". It is essentially multiplayer solitaire.

Kings and Friends uses Flask-SocketIO for Python and runs on an AWS EC2 instance. 

<img src="https://github.com/AndrewAJoh/Kings-and-Friends/blob/master/Kings.PNG">

### Game Structure
* The game will only start when four players have joined.
  * Turn order is dictated by the order in which players joined.
* The game will continue to run until a player runs out of cards, or only one player remains.
* If you are not in the game, you can spectate and see the cards on the table.
* Players select and move cards by clicking on them.
  * A player can only move when it is their turn, indicated by the table on the left.
* When a player wins, their name gets added to the "Hall of Fame".
  * A player will not get a win if all other players disconnect.
  * The players with the top three scores will get a gold, silver, and bronze name.
* After the game is over, all players and spectators are given the opportunity to join the new game.
