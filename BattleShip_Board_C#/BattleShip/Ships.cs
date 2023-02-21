using System;
using System.Collections.Generic;

namespace BattleShip
{
    class Ships
    {

        public Dictionary<string, Tuple<int, int, char>> Boats
         = new Dictionary<string, Tuple<int, int, char>>
                 {
                     {Con.CARRIER, Tuple.Create(5, 0, 'C')},
                     {Con.BATTLESHP, Tuple.Create(4, 1, 'B')},
                     {Con.DESTROYER, Tuple.Create(3, 2, 'D')},
                     {Con.SUB, Tuple.Create(3, 3, 'S')},
                     {Con.PATROL, Tuple.Create(2, 4, 'P')},
                 };


            



    }

}
