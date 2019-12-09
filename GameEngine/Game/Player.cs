using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace Game
{
    public class Player
    {
        public string PlayerName;
        public int Points;
        public int CardsInHand;
        [JsonProperty]
        private List<Card> Cards;
        //The order in which they joined for now. This is how we display the "circle" of players.
        public int Id;

        public Player(string playerName, int id)
        {
            PlayerName = playerName;
            Points = 0;
            CardsInHand = 0;
            Cards = new List<Card>();
            Id = id;
        }

        public void AddCard(Card card)
        {
            Cards.Add(card);
            CardsInHand++;
        }
    }
}
