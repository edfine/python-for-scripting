# In addition to creating errors, Python allows programmers to anticipate
# when exceptions might occur, and run special code that either handles the 
# exception, or allows the program to terminate more gracefully.

# The try/except statement creates a block (like loops and if statements)
# if an error occurs within the try block then the program will
# skip ahead to the except block.

# MICRO-EXERCISE: read this code and try to explain what the
# try/except block accomplishes. Run the code if it helps.
while True:
    try:
        x = float(input("Type a number: "))
        break
    except:
        print("I'm sorry, that was not a number.")

print(f'Good job, {x} is a number!')


# In the above code ANY exception is handled in the same way.
# except blocks can specify which exceptions should be handled:
while True:
    try:
        x = float(input("Type a number that isn't zero: "))
        y = 10 / x
        print("well done!")
        break
    except ValueError:
        print("Sorry, that was not a number. Try again.")
    except ZeroDivisionError:
        print("Sorry, zero is not a valid choice. Try again")


# try/except also supports an "else" block which only executes if 
# no exception was thrown, the following is functionally equivalent 
# to the last example, but uses else:
while True:
    try:
        x = float(input("Type a number: "))
        y = 10 / x
    except ValueError:
        print("Sorry, that was not a number. Try again.")
    except ZeroDivisionError:
        print("Sorry, zero is not a vaild choice. Try again")
    else:
        print("well done!")
        break

# try/except also supports a "finally" block, which ALWAYS executes
# either after the relevant except block has completed, or after the 
# try block has completed successfully. 

# MICRO-EXERCISE: Try to predict how "break" and "finally" will interact
# in this code. Then run the code and find out!
while True:
    try:
        x = float(input("Type a number: "))
        y = 10 / x
    except ValueError:
        print("Sorry, that was not a number. Try again.")
    except ZeroDivisionError:
        print("Sorry, zero is not a vaild choice. Try again")
    else:
        print("well done!")
        break
    finally:
        print("Executing finally")

# Note that: finally has similar interactions with continue and return, read more here: 
# https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions