#! python3

str1 = 'This is a string. It uses single quotes.'
str2 = "This is a string, too. But it uses double quotes."
str3 = '''This uses triple quotes
so that it can span multiple lines of code.'''

# Note: You can use double quotes for triple strings, too.

# sep='some_value' is a parameter that "separates" 
# This separates each string with a newline 
# So, instead of print(str1) print(str2) print(str3), everything can be done at once
print(str1, str2, str3, sep='\n')
