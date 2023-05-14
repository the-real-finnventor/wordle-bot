from basic_wordle_bot import *
first_guess_file = open('/Users/realfinnventor/Desktop/best_word.txt','r')
first_guess = first_guess_file.readline()


def elim(guesses:list,result:list,guess:str)->list:
    valid_guesses = []
    for word in guesses:
        if check_word(word,guess,result) == True:
            valid_guesses.append(word)
    return valid_guesses


def find_best_guess(guesses:list)->str:
    min_avg_remain = 1_000_000_000
    best_guess = ''
    for guess in guesses:
        remain = 0
        for word in guesses:
            result = wordle(guess,word)
            valid_guesses = elim(guesses,result,guess)
            remain += len(valid_guesses)
        avg_remain = remain / len(guesses)
        if avg_remain < min_avg_remain:
            min_avg_remain = avg_remain
            best_guess = guess
    return best_guess


if __name__ == '__main__':
    for i in range(6):
        # First guess is random, and 2-6 are random but can only be possible guesses
        if i == 0:
            guess = first_guess
        else:
            guess = find_best_guess(guesses)
        print(f'Type in {guess}')
        word = input('What word did you type in?: ').lower()
        if word != '':
            guess = word
        colors = input('Enter colors:\n     x = gray    y = yellow    g = green:\n').lower()
        run = 0
        result = []
        while True:
            if colors[run] == 'x':
                result.append('gray')
                run += 1
            elif colors[run] == 'y':
                result.append('yellow')
                run += 1
            elif colors[run] == 'g':
                result.append('green')
                run += 1
            else:
                print('Please enter valid color string')
                colors = input('Enter colors:\n     x = gray    y = yellow    g = green:\n').lower()
                run = 0
                result = []
            if run == 5:
                break
        # Check if guess is correct
        if is_correct(result) == True:
            print("win")
            break
        # Eliminate all invalid guesses
        valid_guesses = []
        for word in guesses:
            if check_word(word,guess,result) == True:
                valid_guesses.append(word)
        print(f"{len(valid_guesses)} valid guesses remain")
        guesses = valid_guesses