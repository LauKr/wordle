import numpy as np
from termcolor import colored


# --- Config --- #
NUM_TRY = 6
VALIDATE = False
LANG = 'en'  # currently, only supported language
# ---        --- #


def main(filename):
    all_possible_words = np.genfromtxt(filename, delimiter='', dtype='str', usecols=[0])
    all_possible_words = np.char.upper(all_possible_words)
    correct_word = np.random.choice(all_possible_words)
    if VALIDATE:
        valid_words = np.genfromtxt('word_lists/wordle-allowed-guesses.txt', delimiter='', dtype='str', usecols=[0])
        valid_words = np.char.upper(valid_words)
    for _ in range(NUM_TRY):
        while True:
            user_input = input('Guess: ')
            if user_input.isalpha():
                if len(user_input) == 5:
                    user_input = user_input.upper()
                    if VALIDATE:
                        if user_input in (valid_words or all_possible_words):
                            break
                        else:
                            print('Not in list')
                    else:
                        break
                else:
                    print('Input should be exactly 5 letters ;)')
            else:
                print('Input should be only letters ;)')

        user_colors = []
        if user_input == correct_word:
            print(colored(user_input[0], 'green'), colored(user_input[1], 'green'),
                  colored(user_input[2], 'green'), colored(user_input[3], 'green'),
                  colored(user_input[4], 'green'))
            break
        for i, char in enumerate(user_input):
            if char in correct_word:
                if char == correct_word[i]:
                    user_colors.append('green')
                else:
                    user_colors.append('yellow')
            else:
                user_colors.append('grey')

        print(colored(user_input[0], user_colors[0]),
              colored(user_input[1], user_colors[1]),
              colored(user_input[2], user_colors[2]),
              colored(user_input[3], user_colors[3]),
              colored(user_input[4], user_colors[4]))
    print('Correct word was: {}'.format(correct_word))
    return 0


if __name__ == '__main__':
    print("Try guessing a word! If a letter is correct, it appears green, if it is contained in the correct word but",
          "at another position, it's green and if it's not included in the correct word it's grey.")
    if LANG == 'de':
        file = 'word_lists/wordle-answers-alphabetical.txt'  # CHANGE TO GERMAN as soon as available
    else:
        file = 'word_lists/wordle-answers-alphabetical.txt'
    main(file)
