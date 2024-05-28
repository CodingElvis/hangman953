# Hangman Game

import random

#define the word list for the game. substituting here  would let the game be played with a different selection of words
word_list = ["apple", "banana", "peach", "strawberry", "lemon"]

class Hangman:
    '''
    This class establishes objects that operate a hangman game.
    
    Attributes passed to the constructor by the user:
    - self.word_list : a list of words, passed to the class constructor as first argument, defining the words the computer picks from (required)
    - self.num_lives : count of number of lives remaining, can be initialised by a second argument in class constructor, or defaults to 5 initial lives
    
    Attributes initialised by the constructor:
    - self.word : a random selection from self.word_list, being the word the player will try to guess, which is cast to lower case
    - self.word_guessed : a list (of strings) representation of the word to be guessed, showing the word length, and any letters already guessed;
    - self.num_letters : the number of unique letters still to be guessed (initialised as number of unique letters in the chosen word)
    - self.list_of_guesses : a list tracking guesses already made, initially an empty list
    '''
    
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This method checks whether a player's guess (passed as an argument) is in the word to be guessed.  
        If it is, the method updates the visible word that the player needs to guess with the new letter and adjusts the number of remaining letters to be guessed.
        If it is not, the method updates the number of lives remaining.
        In both cases, the player is informed, and the list of letters guessed is updated with the new guess
        
        The parameter guess should be a single lower case alphabetical character, which we confirm before calling this method
        '''   
        
        if guess in self.word:
            print (f"Good guess! {guess} is in the word.")
            for i in range (len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        '''
        This method asks the user to guess a letter, which is cast to lower case.
        The guess must be valid, which means it must be a single alphabetical character not already guessed.
        If the guess is not valid, the loop again asks for a user input.
        If the guess is valid, the check_guess() method is called, and the guess is added to our list of guessed characters.
        '''

        while True:
            guess = input ("Please guess a letter: ")
            guess = guess.lower()
            if  len (guess) != 1 or guess.isalpha()==False:
                print("Invalid letter.  Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess (guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list, num_lives=5):
    '''
    This function sets up and runs a game of Hangman.

    First the Hangman class is called to set up an instance of the Hangman game.
    We then repeatedly ask for guesses, and check whether they're in the word, until the game's win or loss condition is satisfied.
    At each iteration information about the "state of the game" is printed to the terminal.

    The function has two parameters:
    - a list of words that will be used as the basis for the game (required)
    - the number of lives for the player (optional, defaults to 5 if unspecified)    
    '''
    
    game = Hangman(word_list, num_lives)
    round = 1
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was {game.word}")
            break
        elif game.num_letters > 0:
            print()
            print (f"Round: {round} Lives remaining: {game.num_lives}")
            print (f"Word to guess: {' '.join(game.word_guessed)}")
            print (f"Previous guesses : {game.list_of_guesses}")
            game.ask_for_input()
            round +=1
        else: 
            print("Congratulations.  You won the game.")
            print(f"The word was {' '.join(game.word_guessed)}")

            break

if __name__ == "__main__":
    play_game(word_list)