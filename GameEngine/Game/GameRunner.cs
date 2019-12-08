using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

namespace Game
{
    public class GameRunner
    {
        public GameStatus GameStatus;
        public GameRunner()
        {
            GameStatus = new GameStatus();
            Start();
        }
        public GameStatus Start()
        {
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
            return GameStatus;
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

        //public GameStatus PlaceCard()
        //{
        //
        //}

        public GameStatus DrawCard(int playerId)
        {
            GameStatus.DrawFromDeck(playerId);
            return GameStatus;
        }

        public GameStatus AddPlayer(string playerName)
        {
            GameStatus.AddPlayer(playerName);
            return GameStatus;

        }

        public int GetPlayerCount()
        {
            return GameStatus.GetPlayerCount();
        }
    }
}
