# We often have values that should be grouped.
# Python offers two main "collections" for such cases:
# the list and the dictionary.

# Lists are an ordered collection of items.
# We can make a new one using square brackets: []
empty_list = []
l_one = [1, 2, 3, 4, 5, 6]
l_two = ['a', 'b', 'c', 'd', 'e', 'f']

# We choose the order, so this is perfectly allowed:
l_three = [6, 1, 2, 5, 4, 3]

# We can fetch a particular item from the list using "bracket notation"
# Programmers pronounce this line of code "print l_one sub zero" and it
# returns the item in the first position of the list, which is the number 1.
print(l_one[0])

# So what does this print?
print(l_two[3])

# What about this?
print(l_three[-1])

# Bracket notation can also be used to modify values in the list
l_one[0] = 999
print(l_one)

# What about this? (Hint: it's commented out for a reason...)
# print(l_three[6])

# Lists have many useful functions built in that we can use, such as 
# append for adding an item to the end of a list, and the len function
# for determining how many items are in a list. See the docs for more:
# https://docs.python.org/3/tutorial/datastructures.html
new_list = []
new_list.append('hello')
new_list.append('good')
new_list.append('people')

print("\n", new_list, len(new_list))

# looping over lists is easy in Python with the "for loop"
print("\nFor l_one: ")
for i in l_one:
    print(i)

print("\nFor l_two: ")
for i in l_two:
    print(i)

print("\nFor l_three: ")
for i in l_three:
    print(i)

# We can nest loops by placing one loop indented inside another.
# In this case the inner loop runs to completion once per outer loop. 
# The range function (essentially) creates a list starting at 0 with
# the number of items specified, for example range(3) => [0, 1, 2].
for i in range(10):
    print(i)
    
    for j in range(10):
        print ("   ", j)

print(new_list)

# Micro-Exercise: append three more values to new_list, then loop
# over all the values in new_list and for each value print the 
# value AND type.
