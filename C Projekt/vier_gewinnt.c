#include <stdio.h>
#include <iostream>
using namespace std;


const int ROWS = 6, COLS = 7;
int x, y, userRow, userCol;
bool player_1 = false;
bool gameRunning = true;

bool checkWin(char gameBoard[][COLS], char playerSymbol){

  //check horizontal
  for (x = 0; x < ROWS; ++x){
    for (y = 0; y <= COLS - 3; ++y) {
      if (gameBoard[x][y] == playerSymbol && gameBoard[x][y] == gameBoard[x][y+1] && gameBoard[x][y+1] == gameBoard[x][y+2] && gameBoard[x][y+2] == gameBoard[x][y+3]){
        return true;
      }
    }
  }
  //check vertical
  for (x = 0; x <= ROWS - 3; ++x){
    for (y = 0; y < COLS; ++y) {
      if (gameBoard[x][y] == playerSymbol && gameBoard[x][y] == gameBoard[x+1][y] && gameBoard[x+1][y] == gameBoard[x+2][y] && gameBoard[x+2][y] == gameBoard[x+3][y]){
        return true;
      } 
    }
  }
  //check diagonal (left to right)
  for (x = 0; x <= ROWS - 3; ++x){
    for (y = 0; y <= COLS - 3; ++y) {
      if (gameBoard[x][y] == playerSymbol && gameBoard[x][y] == gameBoard[x+1][y+1] && gameBoard[x+1][y+1] == gameBoard[x+2][y+2] && gameBoard[x+2][y+2] == gameBoard[x+3][y+3]){
        return true;
      } 
    }
  }
  //check diagonal (right to left)
  for (x = 0; x <= ROWS - 3; ++x){
    for (y = COLS - 1; y > 2; --y) {
      if (gameBoard[x][y] == playerSymbol && gameBoard[x][y] == gameBoard[x+1][y-1] && gameBoard[x+1][y-1] == gameBoard[x+2][y-2] && gameBoard[x+2][y-2] == gameBoard[x+3][y-3]){
        return true;
      } 
    }
  }

  return false;
}

void printBoard(char gameBoard[][COLS]){
  cout << "      ";
  for (y = 0; y < COLS; y++){
    cout << y << " ";
  }
  cout << '\n';
  for (x = 0; x < ROWS; x++){
    cout << "   " << x << "  ";
    for (y = 0; y < COLS; y++){
      cout <<  gameBoard [x][y] << " ";
    }
    cout << '\n';
  }
}


void turn(char gameBoard[][COLS], int player){
  char playerSymbol;

  if (player == 1){
    playerSymbol = 'x';
  } 
  if (player == 2) {
    playerSymbol = 'o';
  }
  cout << "\nPlayer " << player << " turn (" << playerSymbol << "): \nRow: ";
  cin >> userRow;
  cout << "Column: ";
  cin >> userCol;

  if (userRow >= ROWS || userCol >= COLS || userRow <= ROWS || userCol <= COLS){
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

int main (void) {
  char gameBoard[ROWS][COLS];

  cout << "Welcome to 'Connect Four'!" << "\n\n" << "The Game-Board: " << "\n\n";

  for (x = 0; x < ROWS; x++){
    for (y = 0; y < COLS; y++){
      gameBoard [x][y] = '_';
    }
  }

  cout <<"      C o l u m n s\n";
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