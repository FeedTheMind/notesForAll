# You will mainly encounter packing and unpacking in functions.

# Double asterisks (**) on a parameter in Python will "pack" the keywords into a dictionary--hence, keyword arguments . . . kwargs
def packer(**kwargs):
    print(kwargs)

packer(name='Some_Name', num=777)
# This will print {'name': 'Some_Name', 'num': 777} to the console.

# But what if a name-value pair is given? . . . 
  # def packer(name='TonyTheTig', **kwargs):
        # print(kwargs)
  # packer(name='Some_Name', num=777) 
  # This will only print {'num': 777} to the console because the name variable has been caught outside the dictionary.
  # Also, keep in mind that **kwargs must be the last parameter of a function definition.

#############################################################

# The parameters with = after them indicate default values.
# So, if no values are given, None will be the default for both.
def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print('Hi, {} {}!'.format(first_name, last_name))
    else:
        print('Hi, no name!')

# Since the keywords are coming from a dictionary, order is not important. And by "order," note how the first_name parameter comes before last_name in the unpacker function, above.
# Also, remember: Double asterisks "unpack" from the dictionary.
unpacker(**{'last_name': 'Some_Last', 'first_name': 'Some_Name'})

######
#Useful websites: https://hangar.runway7.net/python/packing-unpacking-arguments

#http://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
######

#############################################################
print('\n')
# *args, **kwargs . . . if you have both of these as parameters to a function, order is important: *args must come before **kwargs, and **kwargs must be the last parameter.
movie_rating = {'PF': 5, 'RD': 5, 'DP': 4, 'KB': 5, 'KBII': 4}

# movie acts as the key; rating acts as the value (of movie)
for movie, rating in movie_rating.items():
    print("{} scored a {}/5.".format(movie, rating))

# The above code works well; however, since items() creates a tuple, you can unpack.
print('\n')
for group in movie_rating.items():
    # The single asterisk on group will "unpack" the tuple that the items() method produces from the movie_rating dictionary.
    print('{} scored a {}/5'.format(*group))

