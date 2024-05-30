# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Overview
This is an implementation of the Hangman game, where the computer "thinks" of a word and the user tries to guess it. It has been developed as a Python coding project as part of AiCore's Bootcamp in Data Analytics, and follows AiCore guidance. The basic hangman game runs off a limited word list of 5 fruits, defined in the game file.  A more challenging game could be provided by passing a larger list of words.
## Installation
Install by cloning `https://github.com/CodingElvis/hangman953.git`
## Usage
Run the file `basic_hangman.py` to launch a round of the game using the default wordlist and the default number of lives, 5.

In each round of the game the word to be guessed is displayed, with any letters already correctly guessed shown.  The player guesses a further letter, and if correct the letter is "filled in" to the word.  If incorrect, the player loses one of their remaining lives. Rounds continue iteratively until either all letters in the word have been successfully guessed (player wins) or no lives remin (player loses).

ALternative versions of the game could be played using different lists of words, or numbers of lives.  Call the `play_game()` function in `basic_hangman.py` passing a wordlist as first argument (required) and number of lives as second argument (default 5).


## File Structure

└───hangman953

    │   .gitignore
    │   basic_hangman.py
    │   README.md
    │
    └───milestones
            milestone_2.py
            milestone_3.py
            milestone_4.py
            milestone_5.py

## Licence
MIT Licence