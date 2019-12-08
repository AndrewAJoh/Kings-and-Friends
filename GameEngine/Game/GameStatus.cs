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
            PlayerTurn = 0;
            id = 1;
            CardList = new List<Card>()
            {
                new Card("D", Rank.Ace, 5),
                new Card("D", Rank.Two, 5),
                new Card("D", Rank.Three, 5),
                new Card("D", Rank.Four, 5),
                new Card("D", Rank.Five, 5),
                new Card("D", Rank.Six, 5),
                new Card("D", Rank.Seven, 5),
                new Card("D", Rank.Eight, 5),
                new Card("D", Rank.Nine, 5),
                new Card("D", Rank.Ten, 5),
                new Card("D", Rank.Jack, 5),
                new Card("D", Rank.Queen, 5),
                new Card("D", Rank.King, 5),
                new Card("H", Rank.Ace, 5),
                new Card("H", Rank.Two, 5),
                new Card("H", Rank.Three, 5),
                new Card("H", Rank.Four, 5),
                new Card("H", Rank.Five, 5),
                new Card("H", Rank.Six, 5),
                new Card("H", Rank.Seven, 5),
                new Card("H", Rank.Eight, 5),
                new Card("H", Rank.Nine, 5),
                new Card("H", Rank.Ten, 5),
                new Card("H", Rank.Jack, 5),
                new Card("H", Rank.Queen, 5),
                new Card("H", Rank.King, 5),
                new Card("C", Rank.Ace, 5),
                new Card("C", Rank.Two, 5),
                new Card("C", Rank.Three, 5),
                new Card("C", Rank.Four, 5),
                new Card("C", Rank.Five, 5),
                new Card("C", Rank.Six, 5),
                new Card("C", Rank.Seven, 5),
                new Card("C", Rank.Eight, 5),
                new Card("C", Rank.Nine, 5),
                new Card("C", Rank.Ten, 5),
                new Card("C", Rank.Jack, 5),
                new Card("C", Rank.Queen, 5),
                new Card("C", Rank.King, 5),
                new Card("S", Rank.Ace, 5),
                new Card("S", Rank.Two, 5),
                new Card("S", Rank.Three, 5),
                new Card("S", Rank.Four, 5),
                new Card("S", Rank.Five, 5),
                new Card("S", Rank.Six, 5),
                new Card("S", Rank.Seven, 5),
                new Card("S", Rank.Eight, 5),
                new Card("S", Rank.Nine, 5),
                new Card("S", Rank.Ten, 5),
                new Card("S", Rank.Jack, 5),
                new Card("S", Rank.Queen, 5),
                new Card("S", Rank.King, 5)
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
            //TODO: Add call to update front end view for all players
        }

        public void DrawFromDeck(int playerId)
        {
            var deck = CardList.Where(c => c.Position == 5).ToList();
            Random rnd = new Random();
            Card card = deck[rnd.Next(0, (deck.Count()))];
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

            //player joins lobby -> calls playerAdd
            //game waits until there are four players and begins
            //game gives 7 cards to each of the players

                    //Choose at random player to go first - this player has order of 0 [0, 1, 2, 3]

            //Cards will be pulled from location 5 at random and given another location("shuffling")
            //TODO: Have a list of cards that you selectively pick off and "shuffle" into this dictionary with it's correct placement (not just all 5). Then it should work.

            //Might be hard to query these by value? but we need to maintain a strict key system

            //pick shuffler
            //
            //var rand = new Random();
            //int randomCardNumber = rand.Next(0, _cardLocations.Count-1);
            //TEST***************

            //TEST***************
            //_cardLocations.RemoveAt(randomCardNumber);    Will not work

            //possible methods:
            //for speed sake we may need to have this on the front end.. are we really going to sit there for 2 full seconds after clicking a move to figure out whether it's valid or not?
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
