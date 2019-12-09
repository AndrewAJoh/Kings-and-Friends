using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Game
{
    public class GameStatus
    {
        [JsonProperty]
        private List<Card> CardList;
        [JsonProperty]
        private List<Player> PlayerList;
        [JsonProperty]
        private int PlayerTurn;
        [JsonProperty]
        private static int id;

        public GameStatus()
        {
            PlayerList = new List<Player>();
            PlayerTurn = 1;
            id = 1;
            CardList = new List<Card>()
            {
                new Card(0, "D", Rank.Ace, 5),
                new Card(1, "D", Rank.Two, 5),
                new Card(2, "D", Rank.Three, 5),
                new Card(3, "D", Rank.Four, 5),
                new Card(4, "D", Rank.Five, 5),
                new Card(5, "D", Rank.Six, 5),
                new Card(6, "D", Rank.Seven, 5),
                new Card(7, "D", Rank.Eight, 5),
                new Card(8, "D", Rank.Nine, 5),
                new Card(9, "D", Rank.Ten, 5),
                new Card(10, "D", Rank.Jack, 5),
                new Card(11, "D", Rank.Queen, 5),
                new Card(12, "D", Rank.King, 5),
                new Card(13, "H", Rank.Ace, 5),
                new Card(14, "H", Rank.Two, 5),
                new Card(15, "H", Rank.Three, 5),
                new Card(16, "H", Rank.Four, 5),
                new Card(17, "H", Rank.Five, 5),
                new Card(18, "H", Rank.Six, 5),
                new Card(19, "H", Rank.Seven, 5),
                new Card(20, "H", Rank.Eight, 5),
                new Card(21, "H", Rank.Nine, 5),
                new Card(22, "H", Rank.Ten, 5),
                new Card(23, "H", Rank.Jack, 5),
                new Card(24, "H", Rank.Queen, 5),
                new Card(25, "H", Rank.King, 5),
                new Card(26, "C", Rank.Ace, 5),
                new Card(27, "C", Rank.Two, 5),
                new Card(28, "C", Rank.Three, 5),
                new Card(29, "C", Rank.Four, 5),
                new Card(30, "C", Rank.Five, 5),
                new Card(31, "C", Rank.Six, 5),
                new Card(32, "C", Rank.Seven, 5),
                new Card(33, "C", Rank.Eight, 5),
                new Card(34, "C", Rank.Nine, 5),
                new Card(35, "C", Rank.Ten, 5),
                new Card(36, "C", Rank.Jack, 5),
                new Card(37, "C", Rank.Queen, 5),
                new Card(38, "C", Rank.King, 5),
                new Card(39, "S", Rank.Ace, 5),
                new Card(40, "S", Rank.Two, 5),
                new Card(41, "S", Rank.Three, 5),
                new Card(42, "S", Rank.Four, 5),
                new Card(43, "S", Rank.Five, 5),
                new Card(44, "S", Rank.Six, 5),
                new Card(45, "S", Rank.Seven, 5),
                new Card(46, "S", Rank.Eight, 5),
                new Card(47, "S", Rank.Nine, 5),
                new Card(48, "S", Rank.Ten, 5),
                new Card(49, "S", Rank.Jack, 5),
                new Card(50, "S", Rank.Queen, 5),
                new Card(51, "S", Rank.King, 5)
            };
        }

        public int GetPlayerCount()
        {
            return PlayerList.Count;
        }

        //AddPlayer will be called once when each person joins
        public void AddPlayer(string playerName)
        {
            PlayerList.Add(new Player(playerName, id));
            id++;
            if   (PlayerList.Count() == 4)
            {
                Deal();
            }
        }

        //Deal is called only once per game when four players have joined
        public void Deal()
        {
            foreach (var player in PlayerList)
            {
                for (var i = 0; i < 7; i++)
                {
                    DrawFromDeck(player.Id);
                }
            }
            //Initialize first cards on the table
            MoveCard(SelectFromDeck(), 2);
            MoveCard(SelectFromDeck(), 4);
            MoveCard(SelectFromDeck(), 6);
            MoveCard(SelectFromDeck(), 8);
            //TODO: Add call to update front end view for all players
        }

        //Returns the ID of a randomly selected deck card
        public int SelectFromDeck()
        {
            var deck = CardList.Where(c => c.Position == 5).ToList();
            Random rnd = new Random();
            Card card = deck[rnd.Next(0, (deck.Count()))];
            return card.Id;
        }

        //Gives the player with the playerId a card randomly chosen from the deck
        public void DrawFromDeck(int playerId)
        {
            var card = CardList.Where(c => c.Id == SelectFromDeck()).Single();
            var player = PlayerList.Where(p => p.Id == playerId).Single();
            player.AddCard(card);
            UpdateCardPosition(card, playerId+10);
        }

        public void UpdateCardPosition(Card card, int position)
        {
            CardList[CardList.IndexOf(card)].Position = position;

        }

        public Player GetPlayerById(int id)
        {
            return PlayerList.Where(p => p.Id == id).Single();
        }

        public int GetPlayerTurn()
        {
            return PlayerTurn;
        }

        public void EndTurn(int playerId)
        {
            if (PlayerTurn == 4){
                PlayerTurn = 1;
            }
            else
            {
                PlayerTurn++;
            }
        }

        //Valid move logic will most likely be in a different method
        public void MoveCard(int cardId, int endLocation)
        {
            var card = CardList.Where(c => c.Id == cardId).Single();
            card.Position = endLocation;
        }

            //player joins lobby -> calls playerAdd
            //game waits until there are four players and begins
            //game gives 7 cards to each of the players
            //Player order determined by who joined first. Player IDs are [1, 2, 3, 4], same with turn.

            //TEST***************

            //TEST***************

            //possible methods:
            //maybe return a pre calculated list of valid moves for quick validation to the front? "Valid moves: 1, 4, 5"

            //Idea: After each move the back end queries a list of the lowest card for each pile. This way we don't have to query the dictionary a hundred times each move, increasing speed

            //IsValidMove(playercard card, int location):
            //  Calls all of the below methods to find out if this move is possible
            //Is pile blank:
            //  returns true if pile is blank
            //Is pile red:
            //  is the last card in a pile red
            //Is pile black:
            //  is the last card in a pile black
            //Is pile full
            //  is the last card in a pile an ace
            //Is king pile:
            //  Is a king corner

            //PlaceCard(Card card, int location)
            //Draw Card()
            //MoveCard(Card card, int Location)
    }
}
