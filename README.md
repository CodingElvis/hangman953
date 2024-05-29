# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Overview
This is an implementation of the Hangman game, where the computer "thinks" of a word and the user tries to guess it. It has been developed as a Python coding project as part of AiCore's Bootcamp in Data Analytics, and follows template guidance. The basic hangman game runs off a limited word list of 5 fruits, defined in the game file.  A more challenging game could be provided by passing a larger list of words.

## Installation, Usage, File Structure
A single file is required for the game, namely basic_hangman.py in this git repo.  Running the file will launch a round of the game using the default wordlist and the default number of lives, 5.  Alternatively, to run a game call the play_game() function passing 1-2 arguments:
- the list of words that the computer will select from (required)
- the number of lives (optional, defaults to 5 if omitted).

## Licence
MIT Licence