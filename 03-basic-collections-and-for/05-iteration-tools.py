# Python has several built in tools for making certain types of
# looping and iteration easier:

l1 = [4, 1, 2, 3, 6, 5]

# The sorted function makes a copy of a list (or any iterable), then sorts that copy.
l2 = sorted(l1)
print(l1 is l2, l2)

# The sort method sorts a list in place.
l1.sort()
print('\n', l1)

# The split function creates a list from a string given a 'separator' character.
l3 = 'a b c d e'.split(' ')
print('\n', type(l2), l2)

# The join method of strings creates a string from a list, using the 
# string as a join character
s1 = ', '.join(l3)
print('\n', type(s1), s1)

# If you want to join a list that has non-string types, you must first 
# cast the values to strings explicitly. A list comprehension works well:
s2 = ':'.join(str(item) for item in l1)
print('\n', s2)

# Sometimes it is useful to have the index value
# as well as the value from the list. In Python we 
# can use the enumerate function for this:
print("\nenumerate")
for index, value in enumerate(l1):
    print(index, value)


# When you have parallel lists in python, the zip function 
# will allow you to cleanly loop through them. There is no 
# limit on the number of parallel lists)
print("\nzip")
for a, b in zip(l1, l3):
    print(a, b)