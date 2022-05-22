# An important distinction between different data types in Python
# is that some data types are "mutable" and others are "immutable"

# Immutable data types cannot be changed. In Python the following types
# are all immutable:

# All builtin numeric types:
integers = 1
floats = 1.0
complexes = 1j + 2

# Strings:
strings = "Can't touch this"

# Tuples:
tuples = ('immutable', 'baby')

# Booleans:
booleans = True

# And None:
none = None

# Immutability has a few important implications, one of which is that immutable objects
# which are indexable will throw errors if you try to assign a value to an index:
strings[0] = 'h'
tuples[1] = 10

# Pretty much all other types are mutable, including lists:
l = [1,2,3]
l[0] = 10 # which means we can do this.

# Note that, variables that point to immutable objects can be reassigned, though:
booleans = [True, False]
booleans[0] = 10
tuples = 10

# Another important aspect of mutability is the concept of a reference.
# Consider the following and try to predict what the print statement will print:
x = [1, 2, 3]
y = x
y[0] = 99

print(x[0]) # What will this print??

# In this case, the two variables x and y are said to "reference" the same object
# in memory. And since it us mutable when we run y[0] = 10, we change (or mutate)
# that object. Which is why x[0] prints what it does.

# Python has a comparison operator that can tell you if two variables reference 
# the same underlying object:
print(x is y)

# Immutable types don't share this property:
x = 1
y = x
y = x + x

# Predict what the following will print:
print(x)
print(y)
print(x is y)

# Micro-exercise: Read the following code, predict what it will print, and then
# try to explain what this means for immutable and mutable types.
a = 1
b = 1
c = a
print(a is b)
print(b is c)
print(a is c)

d = 'hello'
e = 'hello'
f = d
print(d is e)
print(e is f)
print (f is d)

h = [a, b, c]
i = [a, b, c]
j = h
print(h is i)
print(h == i)

print(i is j)
print(i == j)

print(h is j)
print(h == j)