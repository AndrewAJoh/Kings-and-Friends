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
        private int Turn;
        [JsonProperty]
        private static int id;

        public GameStatus()
        {
            PlayerList = new List<Player>();
            Turn = 0;
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

        public void AddPlayer(string playerName)
        {
            PlayerList.Add(new Player(playerName, id));
            id++;
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
    }
}
