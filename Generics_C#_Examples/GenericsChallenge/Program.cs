using System;

namespace GenericsChallenge
{
    class Program
    {

        static void Main(string[] args)
        {

            Console.Write("Enter an integer: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter an integer: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter an integer: ");
            int c = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter an integer: ");
            int d = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(concat(a, b, c, d));


            Console.Write("Enter a float value: ");
            float f1 = float.Parse(Console.ReadLine());
            Console.Write("Enter a float value: ");
            float f2 = float.Parse(Console.ReadLine());
            Console.Write("Enter a float value: ");
            float f3 = float.Parse(Console.ReadLine());
            Console.Write("Enter a float value: ");
            float f4 = float.Parse(Console.ReadLine());

            Console.WriteLine(concat(f1, f2, f3, f4));
            //TODO Generate Comma Separated List for Floats


            Console.Write("Enter a string value: ");
            string s1 = Console.ReadLine();
            Console.Write("Enter a string value: ");
            string s2 = Console.ReadLine();
            Console.Write("Enter a string value: ");
            string s3 = Console.ReadLine();
            Console.Write("Enter a string value: ");
            string s4 = Console.ReadLine();

            Console.WriteLine(concat(s1, s2, s3, s4));
            //TODO Generate Comma Separated List for string


            Console.Write("Press any key to exit...");
            Console.ReadKey();
        }

        public static String concat<T>(T a, T b, T c, T d)
        {
            return a + ", " + b + ", " + c + ", and " + d; 
        }
        /**static void Main(string[] args)
        {


            int largestInt = 0;
            float largestFlt = 0.0f;
            string largestStr = "";
            Console.Write("Enter an integer value: ");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter an integer value: ");
            int b = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter an integer value: ");
            int c = Convert.ToInt32(Console.ReadLine());

            largestInt = FindLargest<int>(a, b, c);

            Console.WriteLine("Largest int is {0}", largestInt);

            // Find largest float
            Console.Write("\nEnter a float value: ");
            float f1 = float.Parse(Console.ReadLine());
            Console.Write("Enter a float value: ");
            float f2 = float.Parse(Console.ReadLine());
            Console.Write("Enter a float value: ");
            float f3 = float.Parse(Console.ReadLine());

            largestFlt = FindLargest<float>(f1, f2, f3);

            Console.WriteLine("Largest float is {0}", largestFlt);

            // Find largest string
            Console.Write("\nEnter a string value: ");
            string str1 = Console.ReadLine();
            Console.Write("Enter a string value: ");
            string str2 = Console.ReadLine();
            Console.Write("Enter a string value: ");
            string str3 = Console.ReadLine();

            largestStr = FindLargest < (str1, str2, str3);

            Console.WriteLine("Largest string is {0}", largestStr);

            Console.Write("\nPress any key to exit...");
            Console.ReadLine();
        }

        public static T FindLargest<T>(T a, T b, T c)
        where T : IComparable
        {
            if(a.CompareTo(b) > 0 && a.CompareTo(c) > 0)
            {
                return a;
            }
            else if (b.CompareTo(c) > 0)
            {
                return b;
            }
            else
            {
                return c;
            }
        }*/

        /**static void FindLargest<T>(T str1, T str2, T str3)
                               where T : 
        {
            int len1, len2, len3;
            len1 = str1.Length;
        }*/
    }
}
