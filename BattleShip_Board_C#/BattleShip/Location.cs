using System;

namespace BattleShip
{
    class Location
    {
        public String[] usrlocation = new string[Con.NUMBER_OF_SHIPS];

        /**
         * @param c1 a character of any case A-z
         * 
         * This method takes a char converts it to uppercase
         * and then converts it to its ascii value.
         * It subtracts 65. This is the value of 'A'
         * the first letter in the alphabet to give a start position
         * of 0 end position of 25. Good for alphabetizing 
         */
       public int AsciiValAlphaPosition(Char c1)
        {
            c1 = char.ToUpper(c1);
            byte ascii = (byte)c1;
            ascii -= 65;
            return ascii;

        }

        /**
         * Changes a char to an int
         */
        public int CharToInt(char c1)
        {
            return (int)Char.GetNumericValue(c1);
        }
    }
}
