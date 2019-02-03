#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
#include <stdbool.h>
using namespace std;

void printHangman(int numberWrongLetters) {
 switch (numberWrongLetters) {
     case 0 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("\n");
      printf("\n");
      printf("\n");
      printf("\n");
      printf("\n");
      printf("\n");
      printf("____________\n\n");
     break;
     case 1 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 2 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 3 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 4 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |\n");
      printf("  |\n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 5 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |    |\n");
      printf("  |    |\n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 6 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |   \\|\n");
      printf("  |    | \n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 7 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |   \\|/\n");
      printf("  |    | \n");
      printf("  |\n");
      printf("__|_________\n\n");
     break;
     case 8 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |   \\|/\n");
      printf("  |    | \n");
      printf("  |   /\n");
      printf("__|_________\n\n");
     break;
     case 9 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    O \n");
      printf("  |   \\|/\n");
      printf("  |    | \n");
      printf("  |   / \\\n");
      printf("__|_________\n\n");
     break;
     case 10 :
      printf("Anzahl falscher Buchstaben: %d\n\n", numberWrongLetters);
      printf("  _______\n");
      printf("  |/   | \n");
      printf("  |    X \n");
      printf("  |   \\|/\n");
      printf("  |    | \n");
      printf("  |   / \\\n");
      printf("__|_________\n\n");
     break;
 }
}

void append(char* s, char c) {
        int len = strlen(s);
        s[len] = c;
        s[len+1] = '\0';
}

void readFile() {
    ifstream file;
    file.open ("woerter.txt");
    if (!file.is_open()) return;

    string word;
    while (file >> word){
        cout<< word << '\n';
    }
}

int main (void)
{
  readFile();
  char wordToGuess[] = "Beispiel";
  char alreadyGuessed[sizeof(wordToGuess)] = "\0";
  char gameRunning = true;
  char inputCharacter;
  int amountWrongLetters = 0;

  for (int i = 1; i < sizeof(wordToGuess); i++){
    append(alreadyGuessed, '_');
  }

  // Ablauf fC<r aller ersten Eingaabebuchstaben
  cout << "Geben Sie einen Buchstaben ein: " << '\n';
  cin >> inputCharacter;
  cout << "Eingabebuchstabe " << inputCharacter << '\n';
  // alle erratenen Buchstaben einsetzen
    for (int i = 0; i < sizeof (wordToGuess); i++){
	    if (wordToGuess[i] == inputCharacter) {
	        cout << "Buchstabe ist enthalten" << '\n';
	        alreadyGuessed[i] = inputCharacter;
	    }
    }
     // Buchstabe ist nicht enthalten
    if (strchr (alreadyGuessed, inputCharacter) == NULL)	{
        cout << "Der Buchstabe ist nicht im zu erratenden Wort enthalten." << '\n';
        amountWrongLetters += 1;
	}
    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';
    printHangman(amountWrongLetters);
    
    
// Ablauf fC<r alle restlichen Eingabebuchstaben
  while(gameRunning == true){
      
    cout << "Geben Sie einen Buchstaben ein: " << '\n';
    cin >> inputCharacter;

// alle erratenen Buchstaben einsetzen
    for (int i = 0; i < sizeof (wordToGuess); i++){
	    if (wordToGuess[i] == inputCharacter) {
	        cout << "Buchstabe ist enthalten" << '\n';
	        alreadyGuessed[i] = inputCharacter;
	    }
    }
    
    // Buchstabe ist nicht enthalten
    if (strchr (alreadyGuessed, inputCharacter) == NULL)	{
        cout << "Der Buchstabe ist nicht im zu erratenden Wort enthalten." << '\n';
        amountWrongLetters += 1;

	}
    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';
    if (strchr (alreadyGuessed, '_') == NULL)	{
	    gameRunning = false;
	}
	printHangman(amountWrongLetters);
    }
    cout << "Das Spiel ist zu Ende!" << '\n';



}