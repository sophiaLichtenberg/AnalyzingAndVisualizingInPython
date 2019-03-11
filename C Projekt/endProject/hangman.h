#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
#include <stdbool.h>
#include <cstdlib>
#include <bits/stdc++.h>
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

// get the word which the user should guess
string getWordToGuess() {
	// number of words which are in the file
	int totalNumberWords = 0;
	// list which is filled with the words of the file
	vector<string> wordList;
   	ifstream file;
    	file.open ("woerter.txt");
   	if (!file.is_open()) return "file isnt open";

	string word;
	// read words from file and add to list
   	while (file >> word){
		totalNumberWords +=1;
		wordList.push_back(word);        
    }

	// generate random number to choose a word of the list
	int randomIndex = rand() % totalNumberWords;

	// get the word of the list
	return wordList.at(randomIndex);
        
}


// handle user input errors
void handleInputErrors(string input){
	// check if input is a character
	// if input is not a character or longer than just one letter, then the input is false and the user has to enter again
        while(!isalpha(input.at(0)) || input.length() > 1){	
              cout << "Sie muessen einen Buchstaben eingeben! \n";
              cout << "Geben Sie einen Buchstaben ein: " << '\n';
		cin >> input;	      
        }
}

// check if string contains other string
int contains(string s1, string s2){
	std::transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
	std::transform(s2.begin(), s2.end(), s2.begin(), ::tolower);
	if(s1.find(s2) != string::npos){
		return 1; // s2 is part of s1
	}
	return 0; // s2 is NOT part of s1
}

// check whethere a player has won or lost
char checkWinLost(int amountWrongLetters, string alreadyGuessed){
	// check if user has won -> true if he has guessed all letters
    if (contains(alreadyGuessed, "_")==0)	{
	    cout << "Sie haben gewonnen! \342\230\272 \342\230\272 \342\230\272" << '\n';
		return false;
	}
	// player has lost if he has guessed 10 times the wrong character
	if (amountWrongLetters>= 10)	{
	    cout << "Sie haben verloren!" << '\n';
		return false;
	}
	return true;
}

int init_hangman (void){
	
	char gameRunning = true; // state if game is running or not
	string input; // user input is a letter to guess the word
	int amountWrongLetters = 0; // number of wrongly guessed letters
	string alreadyGuessed=""; // saves how many letters are already guessed or still have to be guessed
	string wordToGuess = getWordToGuess(); // word which should be guessed

  
	// fill container with "_" for each letter which has to be guessed  
	for(int i=0; i< wordToGuess.length(); i++){
		alreadyGuessed = alreadyGuessed + "_";
	

	cout << "\n\n" << "Willkommen bei Hangman!" << "\n\n" << "Sie müssen ein Wort erraten. Geben Sie einen Buchstaben dafür ein und drücken Sie enter. Wenn der Buchstabe falsch ist, wird Hangman wachsen.\n\n";
    
	cout << "Aktueller Spielstand:" << alreadyGuessed << "\n";
    // game loop
    while(gameRunning){ 
        cout << "Geben Sie einen Buchstaben ein: " << '\n';
        cin >> input;       
		// handle player input errors
        handleInputErrors(input);

	// insert guessed character 
    for (int i = 0; i < wordToGuess.length(); i++){	
	    if (char(tolower(wordToGuess.at(i)) == tolower(input.at(0)))) {
	        alreadyGuessed.at(i) = wordToGuess.at(i);
	    }
    }
   
     // handle case that character is not in word
    if (contains(wordToGuess, input) == 0)	{
        amountWrongLetters += 1;
	}

    cout << "Aktueller Spielstand: " << alreadyGuessed << '\n';

	// paint hangman
	printHangman(amountWrongLetters);
	cout <<"______________________________________________________________________"<<"\n";
	cout<< "\n\n";

    // check if user has won or lost
	gameRunning = checkWinLost(amountWrongLetters, alreadyGuessed);
    }
}


#endif 
