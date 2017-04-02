# In this .py file, I discuss functions, first-class citizen, and closures.

################################# Nested Functions
# This function, outer(), is an example of a nested function. 
# But what is a nested function? Well, if you guessed that a nested
# function is a function nested in a function, go you! :)

# The "outer" function holds the "inner" function. 
def outer():
    number = 700

    def inner():
        return number

    return inner()

print(outer()) # Prints 700

# Something cool about the code above is that the content of "inner" is hidden from "outer", but "inner" has access to "outer". Wait, what?
# When you create a function and are in the global scope, do you have access to the content of the function? Can you grab a variable from the function?
# Try it.

def test_for_local_variable():
    local_variable = "Can't catch me!"
    return local_variable

# If you try to access the local_variable, you'll be greeted with a NameError message. Uncomment the code and see.

# some_variable = local_variable 

# Why did that happen? Because we don't have access to the local scope. So, when you nest functions, it's, to an extent, the same thing:
# You're creating functions that are inaccessible from one viewpoint, but accessible from another. In other words, the innermost function has access to
# the data in the outermost, but not the other way around.

################################# First-Class Citizen
# Now, the intertesting point about the function below, apply(), is that it has three parameters: func, x, and y.
# This is to illustrate that functions, like other values in Python, can be passed around as so. This is why functions are known as first-class citizens.
def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print(apply(add, 50, 50)) # Prints 100
print(apply(sub, 10, 2)) # Prints 8

# To highlight what just happened, we passed three arguments to the apply() function: add (or sub), 50 (or 10), and 50 (or 2). 
# Each of these values matched with its corresponding parameter. No error was thrown when add or 
# sub was passed. Why is that? Well, to reiterate the point about first-class citizen, functions, like other data, can be manipulated in the same way.
# So, when it comes to strings or integers, you can pass either as arguments, store them in variables, etc. The same with functions!
# You can store a function in a variable, pass it as an argument, and so on. But what does it mean to store a function into a variable?

# Great question. To call a function, you use parentheses after the function name. So, let's say we defined happy as a function. To call happy,
# we would do the following: happy()
# Now, let's say that instead of calling happy and storing the returned value in a variable, we wanted to store the happy function in a variable.
# How would we do that? Remove the parentheses! 

def happy(arg):
    return 'Here is your argument: %s.' % arg

variable = happy
# The above variable looks pretty normal, but if you run . . . 
print(type(variable))
# . . . you'll see <class 'function'>.
# In other words, variable now has the ability to act as happy!

print(variable(300)) # Prints 300

################################# Closures
# So, what is happening with the function below?
# It builds on the previous concept! Notice that the add_six function
# is returning inner without its parentheses. What does that do?
# Bingo! It returns the inner function. But how do we gain access to this function?
# Assign the function to a variable! :) (Head to closure variable.)

def add_six(num):
    def inner():
        return num + 6
    return inner

closure = add_six(10) # Here, we are assigning add_six(10) to closure.

# Like before, if we do:
print(type(closure))
# we will see that closure is a function!
# What do we do to call this function? Add parentheses!
print(closure())
