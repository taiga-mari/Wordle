# win condition: guess the right word in 6 turns
# randomise a list of words
# start game!! prompt
#   - make guess
#   - check is valid (correct length and is a valid)
#   - display characters
#   - check win condition

import requests
import random
import enchant #pip install pyenchant

class colors: # Pascal case for class name
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    NORMAL = '\033[0m'
    MAGENTA = '\u001b[935m'

dict = enchant.Dict("en_US") # name `dict` is already used for built-in class, consider using other other name

def is_valid(guess, word):
    if len(guess) != len(word):
        print("Wrong length")
        return False
    if not dict.check(guess):
        print("Not a valid guess")
        return False
    return True

def display_characters(guess, word):
    for i in range(len(guess)):
        if word[i] == guess[i]:
            print(colors.GREEN + guess[i], end='')
        elif guess[i] in word:
            print(colors.YELLOW + guess[i], end='')
        else:
            print(colors.NORMAL + guess[i], end='')
    print(colors.NORMAL)

def check_win(guess, word, num_guesses):
    if guess == word:
        print("You win!! Congrats")
        return True
    elif num_guesses == 6:
        print("Out of guesses :(")
        print("Answer was: ", word)
        return True
    else:
        print("Incorrect. Try again")
        return False

if __name__ == "__main__":
    url = "https://www.mit.edu/~ecprice/wordlist.100000" #API Endpoint
    response = requests.get(url) # request.Response() => return bytes response
    if not response.raise_for_status() == None:
        print(response.raise_for_status())
    all_words = response.content.splitlines()
    # [item for item in list if condition]
    words = [word for word in all_words if len(word)==5]
    # words = filter(lambda word: len(word) == 5, allWords)

    play_again = True
    while play_again:
        word = random.choice(words).decode("utf-8")
        print("Game start! Correctly guess the word in 6 tries to win!")
        print(word)
        num_guesses = 0
        is_end_game = False
        while not is_end_game:
            prompt = "Guess ({remaining} remaining):".format(remaining = 6-num_guesses)
            guess = input(prompt)

            # check valid
            if not is_valid(guess, word):
                print("Invalid guess")
                continue
            num_guesses += 1

            # display characters
            display_characters(guess, word)

            # check win condition
            is_end_game = check_win(guess, word, num_guesses)

        # prompt replay
        play_again_prompt = input("Play again? Y (yes)")
        play_again = True if play_again_prompt == "Y" else False
