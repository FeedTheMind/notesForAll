#! python3
# Slicing/Indexing
#s[start:stop:step] <-- All arguments are optional
# start = inclusive; stop = exclusive; step = "steps" over

s = 'The trouble is we all think we have time.'

s[0] # Indexes at position 0, which is the first char ('T')

s[5] # Indexes at position 5, which is the sixth char ('r')

s[:4] # Slices, using only the stop position ('The')

s[4:] # Slices, everything from "trouble is we . . . "

s[4: 14] # Start and stop, "trouble"

# Quick way to make a copy
copy = s[:] #

# Neat way to reverse a string

reverse = s[::-1] # start and stop = 0; step = -1
