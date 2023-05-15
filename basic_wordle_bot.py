from wordle import *


guesses = possible_answers


def only_grays(guess:str,result:list,i:int)->bool:
    for j in range(5):
        if guess[i] == guess[j] and result[j] != 'gray':
            return False
    return True


def check_word(word,guess,result):
    word = list(word)
    guess = list(guess)
    for i in range(5):
        if result[i] == "gray" and only_grays(guess,result,i):
            if guess[i] in word:
                    return False
        elif result[i] == 'green':
            if guess[i] != word[i]:
                return False
        elif result[i] == "yellow" or only_grays(guess,result,i) == False:
            if guess[i] == word[i]:
                return False
            if guess[i] not in word:
                return False
    return True


def is_correct(result):
    if result == ['green','green','green','green','green']:
        return True
    return False

if __name__ == '__main__':
    word = random_word(possible_answers)
    for i in range(6):
        # First guess is random, and 2-6 are random but can only be possible guesses
        guess = random_word(guesses)
        result = wordle(guess,word)
        # Check if guess is correct
        if is_correct(result) == True:
            print("win")
            break
        # Eliminate all invalid guesses
        valid_guesses = []
        for word in guesses:
            if check_word(word,guess,result) == True:
                valid_guesses.append(word)
        print(f"{i+1}. {guess}  {result}\t\t{len(valid_guesses)} valid guesses remain")
        guesses = valid_guesses