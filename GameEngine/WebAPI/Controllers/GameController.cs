using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Game;
using Newtonsoft.Json;
using Game.Services;

namespace Kings.Controllers
{

    [Route("api/[controller]")]
    [ApiController]
    public class GameController : ControllerBase {

        //GET api/Game
        [HttpGet]
        public string Get()
        {
            return GameService.Get();
        }

        [Route("Draw")]
        [HttpPost]
        public void DrawCard([FromBody] int playerId)
        {
            GameService.DrawCard(playerId);
        }

        [Route("Join")]
        [HttpPost]
        public string JoinGame([FromBody] string playerName)
        {
            return GameService.PlayerJoin(playerName);
            //Adds player to the list and returns how many players are already in the game. Checks to see if the game can start and starts if so. returns player info to help load other players on front end
            //returns GameStatus in string format
        }


    }
}
