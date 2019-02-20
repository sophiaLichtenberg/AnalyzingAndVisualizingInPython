#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#ifndef vier_gewinnt
#define vier_gewinnt

//Dimensions of the Gameboard
const int ROWS = 6, COLS = 7;
int x, y;
// Boolean, that checks who's turn it is
bool player_1 = false;
// for them main game loop
bool gameRunning = true;

// checks if a player connected 4 of his Symbols 
// in a vertical, horizontal or diagonal 
// direction and returns true if he did otherwise return false

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

// print board after every turn with the Numbers at the side
// for the Columns and Rows

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

// check if user input is longer than 1 (because we expect a digit, so a string of the length 1) -> rekrusive again
// check if that is a digit --> if not -> rekrusive again
// check if Input Number is inside the Game board --> if not --> rekrusive again
// read the input as as String for the check and returns the Integer Value that the user enters
// (for Row = 1 or Column = 2)

int checkUserInput(int player ,char playerSymbol, int row_or_col) {
  string input;

  if (row_or_col == 1){
    cout << "Row: ";
  }
  if (row_or_col == 2){
    cout << "Column: ";
  }

  cin >> input;

  if(input.length() == 1){
    if(isdigit(input[0])){
      // convert string to Integer value
      int temp = atoi(input.c_str());

      if (row_or_col == 1){
        if (temp >= 0 && temp < ROWS){
          return temp;
        } else {
          return checkUserInput(player, playerSymbol, row_or_col);
        }
      }
      if (row_or_col == 2){
        if (temp >= 0 && temp < COLS){
          return temp;
        } else {
          return checkUserInput(player, playerSymbol, row_or_col);
        }
      }
    } else {
      return checkUserInput(player, playerSymbol, row_or_col);
    }
  } else {
    return checkUserInput(player, playerSymbol, row_or_col);
  }

}

// function parameter says which player turn it is (Player 1 has the Symbol 'x' and Player 2 the Symbol 'o')
// read the user input (with checking if valid input)
// EXTRA Check if the turn a player wants to do, was already made --> if yes --> function turn again (rekrusive)
// For every turn function 'checkWin' checks if 4 Symbols got connected, if yes --> gameLoop ends
// if not --> change the player

void turn(char gameBoard[][COLS], int player){
  char playerSymbol;
  int userRow, userCol;

  if (player == 1){
    playerSymbol = 'x';
  } 
  if (player == 2) {
    playerSymbol = 'o';
  }

  cout << "\nPlayer " << player << " turn (" << playerSymbol << "): \n";
  userRow = checkUserInput(player, playerSymbol, 1);
  userCol = checkUserInput(player, playerSymbol, 2);
  
  if(gameBoard[userRow][userCol] == '_') {
    cout << "Set at Position -> " << "(" << userRow << ", " << userCol << ")\n\n";
    gameBoard[userRow][userCol] = playerSymbol;
    printBoard(gameBoard);
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

// initialize the game
// set up the gameBoard and start the turn with player 1
// main game Loop --> gameRunning --> change the players turns until game ends

void init_vier_gewinnt() {
  char gameBoard[ROWS][COLS];

  cout << "\n\n" << "Welcome to 'Connect Four'!" << "\n\n" << "The Game-Board: " << "\n\n";

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

#endif 