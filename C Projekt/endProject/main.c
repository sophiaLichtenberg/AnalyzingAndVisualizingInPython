#include <stdio.h>
#include <iostream>
#include <string.h>
#include "vier_gewinnt.h"
#include "hangman.h"
using namespace std;

bool endGame = false;

void runArcade() {
  string input;

  cout << '\n' << "\342\230\272 Willkommen zur Spiel Arcade \342\230\272"<< "\n\n" ;
  cout << "Was wollen Sie spielen?: (Geben Sie die 1 ein für Hangman und die 2 für Vier gewinnt oder 'e' um das Programm zu beenden)" << '\n';
  cin >> input;

  if(input.length() == 1){
    if(isdigit(input[0])){
        int temp = atoi(input.c_str());
        if(temp == 1){
            init_hangman();
        }
        if(temp == 2){
            init_vier_gewinnt();
        }
        else {
            cout << "\n !!! Invalide Eingabe !!! \n";
            return runArcade();
        }
    }         
    if(input[0] == 'e'){
        endGame = true;
        cout << "\n\342\230\272 GOOD BYE \342\230\272\n\n";
    } else {
        cout << "\n !!! Invalide Eingabe !!! \n";
        return runArcade();
    }
  } else {
    cout << "\n !!! Invalide Eingabe !!! \n";
    return runArcade();
  }

}


int main (void) {
    while (!endGame) {
        runArcade();
    }
}