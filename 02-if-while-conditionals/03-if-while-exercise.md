# Exercise: While and If

This exercise is meant to help you practice using if statements and while loops to control the flow of a programs execution.

## The Exercise:

You will write a short Python script representing a simple number guessing game. Your program will generate a random integer between 1 and 100, and will allow the user to repeatedly guess what number was selected by the computer. After each guess, the user should be told one of five things:

1. They guessed the correct number (which should end the program).
2. They have guessed 10 times without guessing correctly (which should end the program).
3. They guessed a number that was larger than the correct number.
4. They guessed a number that was smaller than the correct number.
5. They entered a value that is not a number (which should not count against their 10 guess limit).

In all cases your program should gracefully handle the users input without raising any errors.

Additionally, while there may be other ways to solve this problem, please use a `while` loop and `if/elif/else` statements to achieve your goal.

## Some Hints

### Random Number Generation

We haven't covered random number generation in Python, but our task can be achieved with just two lines of code:

```python
# The random package is built into python, but must be imported to be used.
import random

# The variable secret_number will be an integer between 1 and 100.
secret_number = random.randint(1, 100)
```

See the Python documentation of the [random package](https://docs.python.org/3/library/random.html) for more information about the random package, which includes numerous functions for generating random data in a variety of ways.

### Prompting for Input

We haven't covered prompting the user for input to the console, but like random number generation it can be done quite simply in Python:

```python
# The variable user_input will contain whatever the user types into the console.
# Additionally, the program will pause execution until the user to presses the enter key.
# The string we pass to the input function will be shown to the user as a prompt
user_input = input("Type some input")
```

Note that the `type` of `user_input` will **always** be a string. See the [`input` function documentation](https://docs.python.org/3/library/functions.html#input) for more information.
