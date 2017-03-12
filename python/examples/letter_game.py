import os # Allows for functionality on the system level
import sys # Like os; allows to talk to Python itself
import random

# Create a list of fruits
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

# Use os import to check property
def clear():
    if os.name == 'nt': # All modern Windows have nt
        os.system('cls')
    else:
        os.system('clear')

# Create function to "draw" to console
def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
    print('')
    
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input('Guess a letter: ').lower()

        # Check if guess is greater than one character
        if len(guess) != 1:
            print('You can only guess a single letter!');
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        # isalpha() checks to see if input is a letter
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False

            if found:
                print("You win!")
                print("The secret word was {}.".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost.")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()
def welcome():
    start = input("Press enter/return to start, or type q to quit. ").lower()

    if start == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

print("Welcome to Letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done)
