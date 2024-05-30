import random

word_list = ["apple", "banana", "peach", "strawberry", "pineapple"]

print (word_list)

word = random.choice(word_list)

print(word)

guess =input("Please enter the letter you wish to guess: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print ("Oops! That is not a valid guess")
    