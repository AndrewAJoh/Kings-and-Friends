using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace Game.Services
{
    public static class GameService
    {
        public static GameStatus GameStatus{get;}

        static GameService()
        {
            GameStatus = new GameStatus();
        }
        public static string Get()
        {
            var output = JsonConvert.SerializeObject(GameStatus);
            return output;
        }

        public static void DrawCard(int playerId)
        {
            GameStatus.DrawFromDeck(playerId);
        }

        public static string PlayerJoin(string playerName)
        {
            if (GameStatus.GetPlayerCount() > 3)
            {
                return "The game is full.";
            }
            else
            {
                GameStatus.AddPlayer(playerName);
                var output = JsonConvert.SerializeObject(GameStatus);
                return output;
            }
        }
    }
}
