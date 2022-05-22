# Tuples are very similar to lists, but they are "immutable"
# which means they cannot be modified once they are created.

# We create tuples with parenthesis:
t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd')

# Just like lists, tuples may hold a mixture of different data types.
t3 = (1, 'a', 2, 'b', True, None)

# Just like lists we can determine the length of a tuple using len
print("===Lengths===")
print(len(t1), len(t2), len(t3))

# Just like lists we can access the individual items in a tuple
# using "bracket notation"
print("===Members===")
print(t1[0])
print(t2[-1])
print(t3[3])

# Just like lists we can use for loops to iterate through a tuple:
print('===looping===')
for item in t1:
    print(item)

# However, if we try to modify one of the members of a tuple an error
# will be raised:
t1[0] = 0

# We are allowed to change the value of the variable t1, though.
# The Tuple, not the variable, is 'immutable.'
t1 = "something else entirely"

# Micro-Exercise: Create a tuple with at least 4 items then use a for
# loop to iterate over the values and print each one.