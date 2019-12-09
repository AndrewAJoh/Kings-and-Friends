using System;
using System.Collections.Generic;

namespace Game
{
    public class Card : IComparable<Card>
    {
        public int Id;
        public string Suit;
        public Rank Rank;
        public int Position;
        public Card(int id, string suit, Rank rank, int position)
        {
            Id = id;
            Suit = suit;
            Rank = rank;
            Position = position;
        }

        public int CompareTo(Card obj)
        {
            if (this.Rank < obj.Rank)
            {
                return -1;
            }
            else if (this.Rank > obj.Rank)
            {
                return 1;
            }
            else return 0;
        }
    }
}
