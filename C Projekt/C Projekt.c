#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
#include <stdbool.h>
using namespace std;

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

  for (int i = 1; i < sizeof(wordToGuess); i++){
    append(alreadyGuessed, '_');
  }

  // Ablauf für aller ersten Eingabebuchstaben
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
	}
    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';
    
    
// Ablauf für alle restlichen Eingabebuchstaben
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

	}
    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';
    if (strchr (alreadyGuessed, '_') == NULL)	{
	    gameRunning = false;
	}
    }
    cout << "Das Spiel ist zu Ende!" << '\n';



}
