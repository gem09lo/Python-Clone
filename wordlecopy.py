#Wordle Clone
#python wordle.py


#secret word - random generate 5 letter word?
#Import alphabet
#Welcome to the game message
#Input user function Enter your guess
#put in variable "guess"
#if statement - if guess = secret word then correct, if not guess again and while loop until correct
#validity - guess must be 5 letters and a word?

#highlighting how many correct? colour scheme
# yellow = correct letter wrong place
# green = correct letter right place
# grey = wrong letter
#prints all letters available then remove the wrong letters used and return letters left
#Count the guesses

def greeting():
    print ("Hello! Welcome to the Wordle game! Guess the word in 6 attempts!")
#greeting()

#words_list = []
#with open('wordle_words.txt') as f:
    #file_data = f.read()
    #for word in file_data:
        #words_list.append(word.upper())
    #words_list = "".join(words_list).split()

#import random
#secret_word = random.choice(words_list)

import pathlib
import random
from string import ascii_letters

def secret_word():
    words_list = []
    with open('wordle_words2.txt') as f:
        file_data = f.read()
        for word in file_data:
            words_list.append(word.upper())
        words_list = "".join(words_list).split()
        for word in words_list:
            if len(word) != 5:
                words_list.pop[word]

    return words_list
    #import random
    #return random.choice(words_list)
secret_word = secret_word()

print(secret_word)

def user_input():
    return(input("Guess a word: ").upper())
#guess = user_input()

def letter_indicator(guess):
    combine_words = list(zip(guess, secret_word))
    correct_letters = []
    misplaced_letters = []
    wrong_letters = []
    for i, j in combine_words:
        if i == j:
            correct_letters.append(i)
        elif i in secret_word:
            misplaced_letters.append(i)
        else:
            wrong_letters.append(i)
    return ("Guess: {} \nCorrect letters: {} \nMisplaced letters: {} \nWrong letters: {}".format(guess, correct_letters, misplaced_letters, wrong_letters))

#greeting()

def game():
    guess = user_input()
    attempts = 1
    while attempts < 6:
        if guess == secret_word:
            print("You\'ve guessed it! The word was {}".format(secret_word))
            break
        else:
            print(letter_indicator(guess))
            print("You have {} attempts left".format(6-attempts))
            guess = user_input()
            attempts += 1
    if guess != secret_word:
        print("Game over - The word was {}".format(secret_word))

game()
