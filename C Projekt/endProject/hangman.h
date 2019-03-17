#include <stdio.h>
#include <fstream>
#include <string.h>
#include <stdlib.h> 
#include <iostream>
#include <stdbool.h>
#include <random>
using namespace std;

#ifndef hangman
#define hangman

void printHangman(int numberWrongLetters) {
 switch (numberWrongLetters) {
     case 0 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "\n";
      cout << "\n";
      cout << "\n";
      cout << "\n";
      cout << "\n";
      cout << "\n";
      cout << "____________\n\n";
     break;
     case 1 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 2 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 3 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 4 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |\n";
      cout << "  |\n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 5 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |    |\n";
      cout << "  |    | \n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 6 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |   \\|\n";
      cout << "  |    | \n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 7 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |   \\|/\n";
      cout << "  |    | \n";
      cout << "  |\n";
      cout << " _|__________\n\n";
     break;
     case 8 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |   \\|/\n";
      cout << "  |    | \n";
      cout << "  |   /\n";
      cout << " _|__________\n\n";
     break;
     case 9 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    O \n";
      cout << "  |   \\|/\n";
      cout << "  |    | \n";
      cout << "  |   / \\\n";
      cout << " _|__________\n\n";
     break;
     case 10 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << "  _______\n";
      cout << "  |/   | \n";
      cout << "  |    X \n";
      cout << "  |   \\|/\n";
      cout << "  |    | \n";
      cout << "  |   / \\\n";
      cout << " _|__________\n\n";
     break;
 }
}

void append(char* s, char c) {
    int len = strlen(s);
    s[len] = c;    
    s[len+1] = '\0';
}

int init_hangman (void){
  char* words[] = { "Beispiel", "Analogie", "Diktator", "Eiscreme", "Erdbeere"};
  int length = 4;
  
  // Random Function
  std::random_device dev;
  std::mt19937 rng(dev());
  std::uniform_int_distribution<std::mt19937::result_type> dist6(0, length);

  char* wordToGuess = words[dist6(rng)];
  char alreadyGuessed[sizeof(wordToGuess)] = "\0";
  char gameRunning = true;
  char inputCharacter;
  string input;
  int amountWrongLetters = 0;

  for (int i = 1; i < sizeof(wordToGuess) +1 ; i++){
    append(alreadyGuessed, '_');
  }


  cout << "\n\n" << "Welcome to 'Hangman'!" << "\n\n";
    
    // Spielablauf
    while(gameRunning == true){
        
        cout << "Geben Sie einen Buchstaben ein: " << '\n';
        cin >> input;
        inputCharacter = input[0];

        //cout << input.length();
        
        // User Input Errors handeln
        while(!isalpha(inputCharacter) || input.length() > 1){// nur genau ein Buchstabe ist der korrekte Input
              cout << "Sie muessen einen Buchstaben eingeben! \n";
              cout << "Geben Sie einen Buchstaben ein: " << '\n';
              cin >> input;
              inputCharacter = input[0];
        }

// alle erratenen Buchstaben einsetzen
    for (int i = 0; i < sizeof (wordToGuess); i++){
	    if (tolower(wordToGuess[i]) == tolower(inputCharacter)) {
	        cout << "Buchstabe ist enthalten" << '\n';
	        alreadyGuessed[i] = wordToGuess[i];
	    }
    }
    
    // Buchstabe ist nicht enthalten
    if ((strchr (alreadyGuessed, tolower(inputCharacter)) == NULL)&&(strchr (alreadyGuessed, toupper(inputCharacter)) == NULL))	{
        cout << "Der Buchstabe ist nicht im zu erratenden Wort enthalten." << '\n';
        amountWrongLetters += 1;
	}
    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';
    // Hangman darstellen
    printHangman(amountWrongLetters);
    // falls alle Buchstaben erraten wurden, dann hat der Spieler gewonnen
    if (strchr (alreadyGuessed, '_') == NULL)	{
	    gameRunning = false;
	    cout << "Sie haben gewonnen!" << '\n';
	}
	// Spieler hat verloren, wenn 10 Buchstaben falsch geraten hat
	if (amountWrongLetters>= 10)	{
	    gameRunning = false;
	    cout << "Sie haben verloren!" << '\n';
	}
    }
}


#endif 