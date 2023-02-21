using System;

namespace BattleShip
{
    class Program
    {
        static void Main(string[] args)
        {
            Board board = new Board();
            String[] ships = { Con.CARRIER, Con.BATTLESHP, Con.DESTROYER, 
                               Con.SUB, Con.PATROL };
            board.rows = Con.ROWS;
            board.columns = Con.COLUMNS;
            board.playboard = new char[board.rows, board.columns];
            board.fill = Con.FILLER;
            board.boarder = Con.BORDER;
            board.InitializeBoardArray();

            //asks for user input for board placement
            Console.Write(board.MakeBoardString());
            for(int i = 0; i < ships.Length; i++)
            {
                RepeatValidate(ships[i], board);
                Console.Write(board.MakeBoardString());
            }



        }

        /**
         * @param ship ship string
         * @param board the board method
         * 
         * validates user input
         */
        static void RepeatValidate(String ship, Board board)
        {
            int n = 0, horv;
            String location;
            String hov;
            var question = new System.Text.StringBuilder();
            question.AppendFormat("Please enter the location for your {0} (ex: C1)", ship);

            //asks user for input checks if valid with placeship
            while (n != 1)
            {
                location = usrinput(question.ToString());
                hov = usrinput("Is this ship oriented horizontally (y/n)?");
                if (string.Equals(hov, "y"))
                    horv = 0;
                else
                    horv = 1;
                if (board.PlaceNewShip(horv, ship, location))
                    n++;
                
            }
        }

        /**
         * @param message gets user input and returns it after printing message
         */
        static String usrinput(String message)
        {
            string usr;
            Console.WriteLine(message);
            usr = Console.ReadLine();
            return usr;
        }













    }
}
