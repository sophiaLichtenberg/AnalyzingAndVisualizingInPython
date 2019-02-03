#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
#include <stdbool.h>
using namespace std;

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
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 2 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 3 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 4 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |\n";
      cout << " |\n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 5 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |    |\n";
      cout << " |    | \n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 6 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |   \\|\n";
      cout << " |    | \n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 7 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |   \\|/\n";
      cout << " |    | \n";
      cout << " |\n";
      cout << "_|__________\n\n";
     break;
     case 8 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |   \\|/\n";
      cout << " |    | \n";
      cout << " |   /\n";
      cout << "_|__________\n\n";
     break;
     case 9 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    O \n";
      cout << " |   \\|/\n";
      cout << " |    | \n";
      cout << " |   / \\\n";
      cout << "_|__________\n\n";
     break;
     case 10 :
      cout << "Anzahl falscher Buchstaben: " << numberWrongLetters << "\n\n";
      cout << " _______\n";
      cout << " |/   | \n";
      cout << " |    X \n";
      cout << " |   \\|/\n";
      cout << " |    | \n";
      cout << " |   / \\\n";
      cout << "_|__________\n\n";
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