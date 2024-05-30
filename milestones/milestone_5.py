# Hangman Game

import random


class Hangman:
    '''
    This class is used to operate a hangman game.
    
    Attributes passed as arguments to constructor
    ---------------------------------------------
    - self.word_list : list of strings (alphabet only)
         Required first argument which defines available game words
    - self.num_lives : int
        counts game lives, optional second argument (default 5)
    
    Attributes initialised by the constructor
    -----------------------------------------
    - self.word : str
        the word to be guessed, randomly chosen from self.word_list
    - self.word_guessed : list of single character strings 
        a printable list showing guessed and unguessed letters
    - self.num_letters : int 
        number of unique letters still to be guessed
    - self.list_of_guesses : list of single character strings
        a list tracking guesses, initially empty
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
        This method checks a player's guess and updates the game.

        Parameters
        ----------
        guess : str
          guessed letter, a single lowercase alphabetical character
        
        Updates
        -------
        - self.word_guessed
        - self.num_letters
        - self.num_lives
        '''
        
        if guess in self.word:
            print (f"Good guess! {guess} is in the word.")
            for index, char in enumerate (self.word):
                if self.word[index] == guess:
                    self.word_guessed[index] = char
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
        '''
        This method obtains a valid guess then calls check_guess()
        
        The method sets up a loop asking for the user to input a guess,
          casts to lower case and checks it is valid (a single 
          alphabetical character not guessed yet. With a valid guess, 
          calls check_guess(), passing this parameter
        
        Parameters
        ----------
        None (calls for user input)

        Returns
        -------
        None but calls check_guess() based on input

        Updates
        -------
        self.list_of_guesses

        '''
        
        while True:
            guess = input ("Please guess a letter: ")
            guess = guess.lower()
            if  len (guess) != 1 or not guess.isalpha():
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

    Uses the Hangman class to set up an instance of the game.  Then
      repeatedly gets and checks guess, until the win or loss condition
      is satisfied.  Prints relevant information on the state of the 
      game each round.

    Parameters
    ----------
    word_list : list of strings, alphabet characters only
      A list of the words to be available in the game     
    '''
    
    game = Hangman(word_list, num_lives)
    round = 1
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was {game.word}")
            break
        elif game.num_letters > 0:
            print (f"\nRound: {round} Lives remaining: {game.num_lives}")
            print (f"Word to guess: {' '.join(game.word_guessed)}")
            print (f"Previous guesses : {game.list_of_guesses}")
            game.ask_for_input()
            round +=1
        else: 
            print("Congratulations.  You won the game.")
            print(f"The word was {' '.join(game.word_guessed)}")
            break


if __name__ == "__main__":
    word_list = ["apple", "banana", "peach", "strawberry", "lemon"]
    play_game(word_list)