# Wordle Clone
# python wordle.py

# validity - guess must be 5 letters and a word?

# highlighting how many correct? colour scheme
# yellow = correct letter wrong place
# green = correct letter right place
# grey = wrong letter
# prints all letters available then remove the wrong letters used and return letters left
# Count the guesses


import random


def greeting():
    print("Hello! Welcome to the Wordle game! Guess the word in 6 attempts!")


def secret_word():
    words_list = []
    with open('wordle_words.txt') as f:
        file_data = f.read()
        for word in file_data:
            words_list.append(word.upper())
        words_list = "".join(words_list).split()
    return random.choice(words_list)


def user_input():
    return (input("Guess a word: ").upper())


def letter_indicator(guess, answer):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> letter_indicator("CRANE", "SNAKE")
    Guess: CRANE
    Correct letters: ['A', 'E'] 
    Misplaced letters: ['N'] 
    Wrong letters: ['C', 'R']
    """
    combine_words = list(zip(guess, answer))
    correct_letters = []
    misplaced_letters = []
    wrong_letters = []
    for i, j in combine_words:
        if i == j:
            correct_letters.append(i)
        elif i in answer:
            misplaced_letters.append(i)
        else:
            wrong_letters.append(i)
    print("Guess: {} \nCorrect letters: {} \nMisplaced letters: {} \nWrong letters: {}".format(
        guess, correct_letters, misplaced_letters, wrong_letters))


def game_over(answer):
    print("Game over - The word was {}".format(answer))


def game():
    greeting()
    answer = secret_word()

    attempts = 1
    while attempts < 7:
        guess = user_input()
        if guess == answer:
            print("You\'ve guessed it! The word was {}".format(answer))
            break
        else:
            print(letter_indicator(guess, answer))
            print("You have {} attempts left".format(6-attempts))
            attempts += 1
    if guess != answer:
        return (game_over(answer))


if __name__ == "__main__":
    game()
