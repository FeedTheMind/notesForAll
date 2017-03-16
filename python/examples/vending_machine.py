#! python3

sodas = ['Soda', 'Pop', 'Fizzy']
chips = ['Crispy', 'Soggy']
candy = ['Sweet', 'Sour', 'Bitter']

while True:
    choice = input('Would you like some SODA, CHIPS, or CANDY?').lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}. Sorry!".format(choice))
    else:
        print("Here's your {}: {}.".format(choice, snack))
