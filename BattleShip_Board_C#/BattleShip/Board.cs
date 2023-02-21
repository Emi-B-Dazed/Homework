using System;

namespace BattleShip
{
    public class Board
    {
        public int rows;
        public int columns;
        public char[,] playboard;
        public char fill;
        public char boarder;
        Ships battleships = new Ships();
        Location locate = new Location();


        /**
         * This param will fill the double array with a char called fill
         * this char will be '.' but can be changed to any other char
         */
        public void InitializeBoardArray()
        {
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                {
                    playboard[i, j] = fill;
                }
            }
        }

        /**
         * @param horv horizontal or verticle
         * @param ship shipstring 
         * @param location a string location of the ship
         */
        public bool PlaceNewShip(int horv, String ship, String location)
        {
            locate.usrlocation[battleships.Boats[ship].Item2] = location;
            int col = locate.AsciiValAlphaPosition(location[0]);
            int row = locate.CharToInt(location[1]);
            int shiplength = battleships.Boats[ship].Item1;
            char shipchar = battleships.Boats[ship].Item3;

            if (ComputeAndValidate(horv, ship, row, col))
            {
                InsertShip(shiplength, shipchar, horv, col, row);
                return true;
            }
            return false;
        }

        /**
         * @param border what char we want to place as a border
         * 
         * This method calls all of the methods which help print out the
         * play board. 
         */
        public String MakeBoardString()
        {
            //We just started learning about these so I'm not sure if I'm
            //using it right or if there should be a buffer already in
            //the string builder.... thoughts for later phases if we continue
            var boardprintout = new System.Text.StringBuilder();

            //This will set up the numbers that go across the top
            boardprintout.Append(NumbersList());

            //call the top/bottom boarder -----------
            boardprintout.Append(TopBottomBoarder());

            //Prints out whatever is in the array at row i column c
            boardprintout.Append(BoardInside());

            //calls top bottom boarder appends it to whole string -------
            boardprintout.Append(TopBottomBoarder());

            //returns string for user to easily read
            return boardprintout.ToString();
        }

        /**
         * enters a ship into the battlefield
         */
        void InsertShip(int shiplength, char ship, int hov, int row, int col)
        {
            int cadd = 0, radd = 0;
            if (hov == 0)
                cadd++;
            else
                radd++;
            for (int i = 0; i < shiplength; i++)
            {
                playboard[row, col] = ship;
                row += radd;
                col += cadd;
            }
        }




        /**
         * @param positrow The index of the row
         * @param positcolumn index of the column
         * @param hov placed horizontally or vertically
         * @param ship what is the ships name
         * 
         * This makes sure there's enough room for a ship to be placed
         */
        public bool ValidateRoom(int positrow, int positcolumn, int hov, string ship)
        {
            int start;
            //this gets the length of the row or column
            int spaceAvailable = playboard.GetLength(hov);
            int shiplength = battleships.Boats[ship].Item1;

            //statement finds if we are moving horizontally or vertically
            if (hov == 1)
                start = positrow;
            else
                start = positcolumn;
            //if the starting position plus the length of the ship
            //is longer than available space it returns false not enough room
            if (start+shiplength < spaceAvailable + 1)
                return true;
            else
                return false;
        }

        /**
         * @param positrow row
         * @param positcolumn col
         * @param hov horizontal or verticle
         * @param ship ship name
         * 
         * This method makes sure the area where the ship
         * is going to be placed is only the filler character
         * and not another ship
         */
        public bool ValidateClear(int positrow, int positcolumn,
                                  int hov, string ship)
        {
            int shiplength = battleships.Boats[ship].Item1;
            int radd = 0, cadd = 0;
            //checks if the incriment is for the row or column
            if (hov == 0)
                cadd++;
            else
                radd++;

            //for loop iterates where the ship will go to ensure
            //that there are no conflicting ships
            for (int i = 0; i < shiplength; i++)
            {
                if (playboard[positrow, positcolumn] != fill)
                    return false;
                positcolumn += cadd;
                positrow += radd;
            }

            return true;
        }

        /**
         * @param hOrV horizontal or verticle
         * @param shipz ship name
         * @param int colstart column
         * @param rowstart row
         * 
         * checks if there's room in the board for a ship and if there's 
         */
        public bool ComputeAndValidate(int hOrV, string shipz, int colstart, int rowstart)
        {
            if (ValidateRoom(rowstart, colstart, hOrV, shipz))
            {
                if (ValidateClear(rowstart, colstart, hOrV, shipz))
                    return true;
            }


            return false;
        }

        /**
          * @param rows number of rows
          * 
          * this one sets up the numbers that are going along the top
          * of the board.
          */
        public String NumbersList()
        {
            var numbers = new System.Text.StringBuilder();

            numbers.Append("    ");
            for (int iterate = 0; iterate < rows; iterate++)
            {
                numbers.AppendFormat("{0}", iterate);
                if (iterate < rows - 1)
                    numbers.Append(" ");
            }
            numbers.Append("\n");

            return numbers.ToString();
        }

        /**
         * @param rows number of rows in a double array
         * 
         * This method creates the top and bottom
         * boarders for the board. They are made of -----s
         */
        public String TopBottomBoarder()
        {
            var boarderstring = new System.Text.StringBuilder();
            boarderstring.AppendFormat("  {0}{1}{2}", boarder, boarder, boarder);
            for (int iterate = 0; iterate < rows; iterate++)
            {
                boarderstring.AppendFormat("{0}{1}", boarder, boarder);
            }
            boarderstring.Append("\n");
            return boarderstring.ToString();
        }

        /**
         * 
         * this method builds the sides and inside of the board.
         * It will iterate through the rows and place
         * the appropriate symbol
         */
        public String BoardInside()
        {
            int AtoZ = 65;
            var innards = new System.Text.StringBuilder();

            //iterates through the rows to place appropriate symbol
            for (int iterate = 0; iterate < rows; iterate++)
            {
                //This adds the appropriate letter for the row
                innards.AppendFormat("{0} | ", (char)(AtoZ + iterate));
                for (int count = 0; count < columns; count++)
                {
                    //inserts the symbol at row iterate column count
                    innards.AppendFormat("{0} ", playboard[iterate, count]);
                }
                //this is the end of the board. Starts a new line
                innards.Append("|\n");
            }

            return innards.ToString();
        }

    }
}
