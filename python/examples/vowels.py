#! python3
def disemvowel(word):
    list_word = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in list_word[:]:
        for vowel in vowels:
            if letter == vowel.upper() or letter == vowel.lower():
                list_word.remove(letter)
    print(''.join(list_word))

disemvowel('Is your name Mario?')
