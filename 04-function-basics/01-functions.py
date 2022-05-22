# Functions are blocks of code that we can reuse.
# We define them using the keyword "def".
# All functions need a name, and optionally may accept parameters.

# This is a function without parameters. 
def compute_two():
    return 1 + 1

# This function has parameters.
def add(parameter_one, parameter_two):
    return parameter_one + parameter_two

# All functions return a value, and if a value is not explicitly
# returned using the return keyword, then None is returned. 

def returns_none_and_does_nothing():
    pass

# We call, or invoke, functions with a similar syntax:
x = compute_two()
y = add(2, 3)
z = returns_none_and_does_nothing()

print(x, y, z)

# We can also pass variables as parameters:
q = add(x, y)
print(q)

# In Python, you can also specify "keyword arguments" which 
# have a name and a default value. All positional arguments 
# must be specified before any keyword arguments. Here, c is a 
# keyword argument.
def uses_keywords(a, b, c = 10):
    return a + b + c

print(uses_keywords(1, 2))      # If unspecified, c uses the default value of 10
print(uses_keywords(1, 2, 3))   # keyword args can be specified positionally, but this is not preferred. 
print(uses_keywords(1, 2, c=3)) # This is the preferred syntax for calling a function with keyword arguments.

# Micro-Exercise: create a function called fancy_math that
# accepts 3 parameters, uses math operators to combine them
# and returns the result of that math. The result should also
# be a number.