using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace Game.Services
{
    public static class GameService
    {
        public static GameRunner GameRunner{get;}

        static GameService()
        {
            GameRunner = new GameRunner();
        }
        public static string Get()
        {
            var output = JsonConvert.SerializeObject(GameRunner.GameStatus);
            return output;
        }

        public static void DrawCard(int playerId)
        {
            GameRunner.DrawCard(playerId);
        }

        public static string PlayerJoin(string playerName)
        {
            if (GameRunner.GetPlayerCount() > 3)
            {
                return "The game is full.";
            }
            else
            {
                var result = GameRunner.AddPlayer(playerName);
                var output = JsonConvert.SerializeObject(result);
                return output;
            }
        }
    }
}
