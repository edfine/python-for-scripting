# Exceptions occur when a programmer asks a program to do something impossible.
# Here are a few examples:

# This line has an unmatched closing parenthesis, which will cause 
# the Python interpreter to fail before even attempting to execute this code.
# In python, the SyntaxError is one of the only errors that prevents code
# from being executed entirely.

# print('hello'))

# In Python, nearly all errors/exceptions are "runtime errors" which means
# They occur after the program has already begun running, unlike the Syntax Error
# which is raised before any lines of code execute.

# 1/0 # Division by zero is, mathematically speaking, impossible. 

# l = [1,2,3]
# l[3] # 3 is "out of bounds" as only indexes 0, 1, and 2 have data.

# The message generated when an exception occurs is called a "stack trace"
# and it usually contains helpful information about what error occurred,
# which line of code generated the error, and the set of functions that 
# were called in order to reach that erroring line of code.

# There are many other built in exceptions... 
# https://docs.python.org/3/library/exceptions.html

# Sometimes a programmer may want to raise an exception themselves.
# A common example would be for ensuring a function is called with
# the appropriate type of data.
def factorial(num):
    if not isinstance(num, int):
        # The raise keyword creates a stack trace 
        raise TypeError(f'factorial expected num to be an integer, but found {type(num)}.')

    factorial_val = 1
    for i in range(2, num+1):
        factorial_val *= i

    return factorial_val


# If we call the function with an integer, everything goes great!
f = factorial(5)
print(f)

# However, if we use any other datatype, our error will be raised
# and the programmer will be able to read our error message.
factorial('hello')

# Note that the stack trace for this error has 2 lines, whereas the previous errors had one line.