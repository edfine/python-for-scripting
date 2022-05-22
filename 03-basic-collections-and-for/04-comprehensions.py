# Comprehensions are a way to quickly create lists and dictionaries 
# using a special syntax. There is not a "tuple comprehensions" syntax.

# This list comprehension generates all the even numbers up to 20
evens = [number for number in range(1, 21) if number % 2 == 0]
print(evens)

# This list comprehension generates the first 10 square numbers
ten_squares = [n*n for n in range(1, 11)]
print(ten_squares)

# Comprehensions are often used to filter existing lists.
# This one filters or list of evens down to numbers that are also divisible by 3.
even_and_div_3 = [even_number for even_number in evens if even_number % 3 == 0]
print(even_and_div_3)

# Comprehensions are also commonly used for processing every value in a list.
# This one formats a list of numbers into a string for display as currency:
currency = [f'${num}.00' for num in evens]
print(currency)

# Dictionary comprehensions use a similar pattern, but the key and value must be specified.
# This one creates a dictionary with keys for the first 10 integers with their square as the value
int_to_square = {i: i*i for i in range(1,11)}
print(int_to_square)

# Dictionary comprehensions also support the if based filtering...
even_squares = {i: i*i for i in range(1,11) if i % 2 == 0}
print(even_squares)

# Micro-exercise: Create a dictionary comprehension that operates over the following
# list of greetings and:
#   * Filters out greetings that do not start with an h.
#   * Uses the greeting value as the key.
#   * Uses True as the value for greetings that use 3 or fewer letters.
#   * Uses False as the value for greetings that use more than 3 letters.
greetings = ['hello', 'hi', 'good morning', 'howdy', 'hey']
