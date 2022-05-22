# There is some interplay between scope and mutability.
# Specifically, when mutable objects are passed into a function
# or when they are returned from a function they remain mutable, 
# even outside the scope they were defined in.

# Or, put another way, Scope is a concept that applies to VARIABLES
# not a concept that applies to the data those variables hold.

def fun1(a):
    a[0] = 'from fun1'

def fun2(b):
    b[1] = 'from fun2'


# Consider the following to see what we mean.
l = [None, None]
fun1(l)
print(l) # Stop: What will this print?

fun2(l)
print(l) # Stop: What will this print?

# While the object in memory (the list) was mutated, the variables a and b
# remain inaccessible in this scope:
# print(a, b) # this line errors.