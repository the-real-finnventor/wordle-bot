from random import choice as random_word
from sys import exit
from wordle_lists import *


def wordle(guess,word):
    if guess not in possible_guesses:
        exit(f"Invalid guess. {guess}")
    guess_letters = list(guess)
    answer_letters = list(word)
    result = []
    for i in range(5):
        if guess_letters[i] == answer_letters[i]:
            result.append("green")
        elif guess_letters[i] in answer_letters:
            result.append("yellow")
        else:
            result.append("gray")
    return result


if __name__ == "__main__":
    word = random_word(possible_answers)
    for i in range(6):
        guess2 = input("please: ")
        print(wordle(guess2,word))