#include <stdio.h>
#include <iostream>
using namespace std;


const int rows = 6, cols = 7;
int x, y, userRow, userCol;
bool player_1 = false;

void turn(char gameBoard[][cols], int player){
  char playerSymbol;

  if (player == 1){
    playerSymbol = 'x';
  } 
  if (player == 2) {
    playerSymbol = 'o';
  }
  cout << "\nPlayer " << player << " turn (" << playerSymbol << "): \nRow: ";
  cin >> userRow;
  cout << "Col: ";
  cin >> userCol;

  if (userRow >= rows || userCol >= cols || userRow <= rows || userCol <= cols){
    if(gameBoard[userRow][userCol] == '_') {
      cout << "Set at Position -> " << "(" << userRow << ", " << userCol << ")\n\n";
      gameBoard[userRow][userCol] = playerSymbol;

      for (x = 0; x < rows; x++){
        cout << "     ";
        for (y = 0; y < cols; y++){
          cout <<  gameBoard [x][y] << " ";
        }
        cout << '\n';
      }
    } else {
      cout << "You can't do this turn\n";
      turn(gameBoard, player);
    }
  } else {
    cout << "You can't do this turn\n";
    turn(gameBoard, player);
  }

  if (player == 1){
    player_1 = false;
  }
  if (player == 2){
    player_1 = true;
  }
};

bool checkWin(char gameBoard[][cols]){
  int i,j;
  int count = 0;

 
  // Loop from 0 to 5 checking its value against player number
    for (int i = 0; i < rows; i++) {
        if (gameBoard[i][cols] == 'o') {
            // If it is the player, count it.

            count++;

            // If it reaches four, you have a win.
            if (count == 4) { return true; }
        }
        else {
            // If any time it doesn't equal player
            // aka empty or other player piece, reset the counter.
            count = 0;
        }
    }
    // Never reached 4, so you have no win yet.
    return false;
/*
  //checks horizontal win
    for(i=0;i<rows;i++)
        for(j=0;j<cols-3;j++)
            if(gameBoard[i][j] != '_' && gameBoard[i][j]==gameBoard[i][j+1] && gameBoard[i][j]==gameBoard[i][j+2] && gameBoard[i][j]==gameBoard[i][j+3])
                return true;
            else
                return false;

    //checks vertical win
    for(i=0;i<rows-3;i++)
        for(j=0;j<cols;j++)
            if(gameBoard[i][j] != '_' && gameBoard[i][j]==gameBoard[i+1][j] && gameBoard[i][j]==gameBoard[i+2][j] && gameBoard[i][j]==gameBoard[i+3][j])
                return true;
            else
                return false;
                

    //checks rigth diagonal win
    for(i=0;i<rows-3;i++)
        for(j=0;j<cols-3;j++)
            if(gameBoard[i][j] != '_' && gameBoard[i][j]==gameBoard[i+1][j+1] && gameBoard[i][j]==gameBoard[i+2][j+2] && gameBoard[i][j]==gameBoard[i+3][j+3])
                return true;
            else
                return false;

    //checks left diagonal win
    for(i=0;i<rows-3;i++)
        for(j=0;j<cols-3;j++)
            if(gameBoard[i][j] != '_' && gameBoard[i][j]==gameBoard[i+1][j-1] && gameBoard[i][j]==gameBoard[i+2][j-2] && gameBoard[i][j]==gameBoard[i+3][j-3])
                return true;
            else
                return false;*/
}

int main (void)
{
  char gameBoard[rows][cols];

  char gameRunning = true;

  cout << "Welcome to 'Connect Four'!" << "\n\n" << "The Game-Board: " << "\n\n";

  for (x = 0; x < rows; x++){
    for (y = 0; y < cols; y++){
      gameBoard [x][y] = '_';
    }
  }

  cout <<"      C o l s      \n";
  cout <<"      0 1 2 3 4 5 6\n";
  cout <<" R 0  _ _ _ _ _ _ _\n";
  cout <<" o 1  _ _ _ _ _ _ _\n";
  cout <<" w 2  _ _ _ _ _ _ _\n";
  cout <<" s 3  _ _ _ _ _ _ _\n";
  cout <<"   4  _ _ _ _ _ _ _\n";
  cout <<"   5  _ _ _ _ _ _ _\n\n";

  turn(gameBoard, 1);
  
  while(gameRunning == true){

    if (player_1){
      turn(gameBoard, 1);
    }
    if (!player_1){
      turn(gameBoard, 2);
    }
    if (checkWin(gameBoard)){
      gameRunning = false;
    }
  }
  cout << "Das Spiel ist zu Ende!" << '\n';

}