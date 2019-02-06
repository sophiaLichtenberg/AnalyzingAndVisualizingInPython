#include <stdio.h>
#include <iostream>
using namespace std;


const int rows = 6, cols = 7;
int x, y, userRow, userCol;
bool player_1 = false;
bool gameRunning = true;

bool checkWin(char gameBoard[][cols], char playerSymbol){

  for (int i = 0; i < rows; ++i){
    for (int j = 0; j <= cols - 3; ++j) {
      if (gameBoard[i][j] == playerSymbol && gameBoard[i][j] == gameBoard[i][j+1] && gameBoard[i][j+1] == gameBoard[i][j+2] && gameBoard[i][j+2] == gameBoard[i][j+3]){
        return true;
      }
    }
  }

  for (int i = 0; i <= rows - 3; ++i){
    for (int j = 0; j < cols; ++j) {
      if (gameBoard[i][j] == playerSymbol && gameBoard[i][j] == gameBoard[i+1][j] && gameBoard[i+1][j] == gameBoard[i+2][j] && gameBoard[i+2][j] == gameBoard[i+3][j]){
        return true;
      } 
    }
  }

  for (int i = 0; i <= rows - 3; ++i){
    for (int j = 0; j <= cols - 3; ++j) {
      if (gameBoard[i][j] == playerSymbol && gameBoard[i][j] == gameBoard[i+1][j+1] && gameBoard[i+1][j+1] == gameBoard[i+2][j+2] && gameBoard[i+2][j+2] == gameBoard[i+3][j+3]){
        return true;
      } 
    }
  }

  for (int i = 0; i <= rows - 3; ++i){
    for (int j = cols - 1; j > 2; --j) {
      if (gameBoard[i][j] == playerSymbol && gameBoard[i][j] == gameBoard[i+1][j-1] && gameBoard[i+1][j-1] == gameBoard[i+2][j-2] && gameBoard[i+2][j-2] == gameBoard[i+3][j-3]){
        return true;
      } 
    }
  }

  return false;
}

void printBoard(char gameBoard[][cols]){
  cout << "      ";
  for (y = 0; y < cols; y++){
    cout << y << " ";
  }
  cout << '\n';
  for (x = 0; x < rows; x++){
    cout << "   " << x << "  ";
    for (y = 0; y < cols; y++){
      cout <<  gameBoard [x][y] << " ";
    }
    cout << '\n';
  }
}


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
      
      printBoard(gameBoard);

    } else {
      cout << "You can't do this turn\n";
      turn(gameBoard, player);
    }
  } else {
    cout << "You can't do this turn\n";
    turn(gameBoard, player);
  }

  if (checkWin(gameBoard, playerSymbol)){
    gameRunning = false;
    cout << "\n\n  ! GAME END ! " << '\n' << "  Player " << player << " won!\n\n";
  } else {
    if (player == 1){
      player_1 = false;
    }
    if (player == 2){
      player_1 = true;
    }
  }
};

int main (void)
{
  char gameBoard[rows][cols];

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
  }

}