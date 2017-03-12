import random
import os 

def clear():
    if os.name == 'nt': # All modern Windows have nt
        os.system('cls')
    else:
        os.system('clear')

def game():

    # random.randint(1, 10) will generate a random number between 1 and 10
    secretNum = random.randint(1, 10)
    # Hold user's guesses
    guesses = []

    while len(guesses) < 5:
        if len(guesses) == 0:
            guess = input('Guess a number between 1 and 10: ')
        else: 
            guess = input('Guess again: ')

        try:
            guess = int(guess)
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            if guess == secretNum:
                print("You got it! My number was {}.".format(secretNum))
                break
            elif guess < secretNum:
                print("My number is higher than {}.".format(guess))
                guesses.append(guess)
            else:
                print("My number is lower than {}.".format(guess))
                guesses.append(guess)
    else:
        print("You didn't get it. My number was {}.".format(secretNum))
    play_again = input("Do you want to play a game again? Y/n ")
    if play_again.lower() != 'n':
        clear()
        game()
    else:
        print("Bye!")
game()
