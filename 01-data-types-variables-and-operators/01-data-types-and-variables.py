# We can create variables by giving them a name, and
# using the assignment operator, the equals sign (=)
# to give them a value.

# Data comes in a variety of types. These two versions
# of the number one are not the same. One is a number, 
# the other is a piece of text.
x = 1
y = '1'

# We can print the "type" of our two variables like this:
print('\n===quotes===')
print(type(x))
print(type(y))

# There are three kinds of numbers in python: integers, floats, and complex numbers
integer_example = 2
float_example = 0.1
complex_example = 4+3j # These are rarely important for most programmers... 

print('\n===number types===')
print(type(integer_example))
print(type(float_example))
print(type(complex_example))

# Booleans are either True or False
t = True
f = False

print('\n===booleans===')
print(type(t))
print(type(f))

# There is a special value that means "nothing"
nothing = None

print('\n===None===')
print(type(nothing))

# And textual data, called strings, are wrapped in quotes
text = "This is a string."
print(type(text))

# Sometimes data of one type can be "coerced" into data of another type
text_number = "20"
coerced_int = int(text_number)
coerced_float = float(text_number)

print("\n===Coercion===")
print(type(text_number), text_number)
print(type(coerced_int), coerced_int)
print(type(coerced_float), coerced_float)

# But, not everything can be coerced
# int("This will cause an error")

# Python also provides a function that can report whether or not a string
# can be coerced to a number without actually attempting the coercion.
can_convert = "123"
print(can_convert, can_convert.isnumeric())

cannot_convert = "I'm not a number"
print(cannot_convert, cannot_convert.isnumeric())

# Micro-Exercise 1: Create a variable and assign it a value.
# Then, pick one of the variables defined above and reassign 
# it to have the same value as the variable you created.
# Prove your code works with a print statement.



# Micro-Exercise 2: try using the bool() and str() functions to coerce some
# non-boolean data into a boolean and some non-string data to a string.
# Perform (at least) 1 such coercion for each of bool() and str() and 
# examine the results using print.