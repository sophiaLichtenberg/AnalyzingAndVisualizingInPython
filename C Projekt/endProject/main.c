#include <stdio.h>
#include <iostream>
#include <limits>
#include <fstream>
#include <string.h>
#include <stdbool.h>

#include "vier_gewinnt.h"
#include "hangman.h"

using namespace std;


int main (void) {
	int choise;

	cout << "\n\n" << "Willkommen zur Spiel Arcade"<< "\n\n" ;
	cout << "Was wollen Sie spielen?: (Geben Sie die 1 ein für Hangman und die 2 für Vier gewinnt)" << '\n';
    cin >> choise;

    if (choise == 1){
    	init_hangman();
	}
    if (choise == 2){
	   	init_vier_gewinnt();
    }
    else {
    	cout << "Falscher Input" << '\n';
    	cin >> choise;
    }
}