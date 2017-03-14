#! python3
import os

shopping_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    clear_screen()
    print('What should we pick up at the store?')
    print('''
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
    ''')


def add_to_list(item):
    if len(shopping_list): # One or more items == true
        position = input('Where should I add {}?\n'
            'Press ENTER to add to the end of the list.\n' 
            '> '.format(item))
    else:
        position = 0

    try: # abs() gets the absolute value of a number; -5 becomes 5
         # if value cannot be converted, set position to None
        position = abs(int(position))
    except ValueError:
        position = None # None is not a number and is easy to compare against
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(item)

    show_list()
    clear_screen()

def show_list():
    clear_screen()

    print('Here\'s your list:')

    index = 1
    for item in shopping_list:
        print('{}. {}'.format(index, item))
        index += 1

        print('-' * 10)

show_help()

holder = True
while holder:

    new_item = input('> ').upper() # Capitalize word(s)--easier to match/see

    if new_item == 'DONE':
        show_list()
        holder = False # Break from loop
    elif new_item == 'HELP':
        show_help()
    elif new_item == 'SHOW':
        show_list()
    else:
        add_to_list(new_item)
        show_list()
