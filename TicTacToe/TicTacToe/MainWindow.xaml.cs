using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace TicTacToe
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        tictactoe T = new tictactoe();
        public MainWindow()
        {
            
            InitializeComponent();
        }

        /*
         * Any time a button in the play area besides reset is clicked this happens
         * @param row the row number of the button
         * @param col the column number of the button
         * @param label the label of the button
         */
        public void clicked(int row, int col, Label label)
        {
            Char XorO;
            char other;
            //checks if button has been used or not
            if (T.IsFree(row, col))
            {
                //checks which player's turn it is
                if (T.getPlayer() == 0)
                {
                    XorO = 'X';
                    other = 'O';
                }
                else
                {
                    XorO = 'O';
                    other = 'X';
                }

                //changes the labels
                label.Content = XorO;
                turn.Content = "It's " + other + "'s turn";
                T.EnterMove(row, col);

                bool win = T.IsWinner(XorO);
                //checks for winners
                if (win)
                {
                    disableButtons();
                    turn.Content = "Winner is: " + XorO + "!";
                    winner.Content = "Press reset\nto play again";
                }

                //checks for cat game
                if (T.CheckFull() && !win)
                {
                    disableButtons();
                    turn.Content = "Cats game :(";
                    winner.Content = "Press reset\nto play again";
                }
            }
        }

        private void zerozero_Click(object sender, RoutedEventArgs e)
        {
            clicked(0, 0, label_00);
        }

        private void zeroone_Click(object sender, RoutedEventArgs e)
        {
            clicked(0, 1, label_01);
        }


        private void zerotwo_Click(object sender, RoutedEventArgs e)
        {
            clicked(0, 2, label_02);
        }

        private void onezero_Click(object sender, RoutedEventArgs e)
        {
            clicked(1, 0, label_10);
        }

        private void oneone_Click(object sender, RoutedEventArgs e)
        {
            clicked(1, 1, label_11);
        }

        private void onetwo_Click(object sender, RoutedEventArgs e)
        {
            clicked(1, 2, label_12);
        }

        private void twozero_Click(object sender, RoutedEventArgs e)
        {
            clicked(2, 0, label_20);
        }

        private void twoone_Click(object sender, RoutedEventArgs e)
        {
            clicked(2, 1, label_21);
        }

        private void twotwo_Click(object sender, RoutedEventArgs e)
        {
            clicked(2, 2, label_22);
        }

        //disables all board buttons except reset
        public void disableButtons()
        {
            zerozero.IsEnabled = false;
            zeroone.IsEnabled = false;
            zerotwo.IsEnabled = false;
            onezero.IsEnabled = false;
            oneone.IsEnabled = false;
            onetwo.IsEnabled = false;
            twozero.IsEnabled = false;
            twoone.IsEnabled = false;
            twotwo.IsEnabled = false;
        }

        //reenables all board buttons clears their content and changes appropriate
        //labels
        private void reset_Click(object sender, RoutedEventArgs e)
        {
            label_00.Content = ' ';
            label_01.Content = ' ';
            label_02.Content = ' ';
            label_10.Content = ' ';
            label_11.Content = ' ';
            label_12.Content = ' ';
            label_20.Content = ' ';
            label_21.Content = ' ';
            label_22.Content = ' ';
            zerozero.IsEnabled = true;
            zeroone.IsEnabled = true;
            zerotwo.IsEnabled = true;
            onezero.IsEnabled = true;
            oneone.IsEnabled = true;
            onetwo.IsEnabled = true;
            twozero.IsEnabled = true;
            twoone.IsEnabled = true;
            twotwo.IsEnabled = true;
            turn.Content = "X's go first";
            winner.Content = "";

            T = new tictactoe();
        }
    }


    public class tictactoe
    {
        public char[,] board = new char[3, 3];
        int player = 0;
        char X = 'X';
        char O = 'O';
        Char fill = ' ';

        //initializes board
        public tictactoe()
        {
            for (int i = 0; i < board.GetLength(0); i++)
            {
                for (int j = 0; j < board.GetLength(1); j++)
                {
                    board[i, j] = fill;
                }
            }
        }

        //checks if the board is full
        public Boolean CheckFull()
        {
            int count = 0;
            for(int i = 0; i < board.GetLength(0); i++)
            {
                for(int j = 0; j < board.GetLength(1); j++)
                {
                    if(board[i, j] != fill)
                    {
                        count++;
                    }
                }
            }

            if (count == board.Length)
                return true;

            return false;
        }

        //enters a new move and switches player
        public void EnterMove(int row, int column)
        {
            if(player == 0)
            {
                board[row, column] = X;
                player++;
            } 
            else
            {
                board[row, column] = O;
                player--;
            }
        }

        //returns what player it is. 0 - X's 1 - O's
        public int getPlayer()
        {
            return player;
        }

        //checks if the spot has an x or o in it already
        public Boolean IsFree(int row, int column)
        {
            if (board[row, column] == ' ')
            {
                return true;
            }
            return false;
        }

        //Checks all possibilities for winning
        public Boolean IsWinner(char winner)
        {
            for (int i = 0; i < board.GetLength(0); i++)
            {
                //across and up and down
                if (board[i, 0] == winner && board[i, 1] == winner && board[i, 2] == winner)
                    return true;

                if (board[0, i] == winner && board[1, i] == winner && board[2, i] == winner)
                    return true;
                
            }
            if (board[0, 0] == winner && board[1, 1] == winner &&
                    board[2, 2] == winner)
                return true;

            if (board[0,2] == winner && board[1,1] == winner &&
                board[2,0] == winner)
                return true;
            return false;
        }



    }
}
