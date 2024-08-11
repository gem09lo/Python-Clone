#Wordle Clone
#python wordle.py

#validity - guess must be 5 letters and a word?

#highlighting how many correct? colour scheme
# yellow = correct letter wrong place
# green = correct letter right place
# grey = wrong letter
#prints all letters available then remove the wrong letters used and return letters left
#Count the guesses

from rich import print
print("Hello, [bold red]Rich[/] :snake:")

from rich.console import Console
console = Console()
console.print("Hello, [bold red]Rich[/] :snake:")

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

from rich.console import Console
console = Console(width=40)
console.rule(":leafy_green: Wyrdle :leafy_green:")

import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

import wordle
wordle.refresh_page("Wordle")
wordle.console.print("Look at me!", style="warning")



import random

def greeting():
    print ("Hello! Welcome to the Wordle game! Guess the word in 6 attempts!")

def secret_word():
    words_list = []
    with open('wordle_words.txt') as f:
        file_data = f.read()
        for word in file_data:
            words_list.append(word.upper())
        words_list = "".join(words_list).split()
    return random.choice(words_list)
secret_word = secret_word()

def user_input():
    return(input("Guess a word: ").upper())

def letter_indicator(guess, secret_word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> letter_indicator("CRANE", "SNAKE")
    Guess: CRANE
    Correct letters: ['A', 'E']
    Misplaced letters: ['N']
    Wrong letters: ['C', 'R']
    """
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

def game_over(secret_word):
    print("Game over - The word was {}".format(secret_word))


def game():
    greeting()
    guess = user_input()

    attempts = 1
    while attempts < 6:
        if guess == secret_word:
            print("You\'ve guessed it! The word was {}".format(secret_word))
            break
        else:
            print(letter_indicator(guess, secret_word))
            print("You have {} attempts left".format(6-attempts))
            guess = user_input()
            attempts += 1
    if guess != secret_word:
        return (game_over(secret_word))

if __name__ == "__main__":
    game()
