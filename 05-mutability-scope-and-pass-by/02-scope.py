# Scope is a term to describe when and where variables are accessible
# in any given program at any given time. The complete details of scope
# can be complex, but for most situations we just need to understand
# Python's 2 main scopes: global and local.

# x is a global scope variable, because it is defined at the "top-level"
# of a file. Specifically we mean that it is defined outside any function.
x = 10

# Function parameters, such as y, belong to the local scope of the function
# that defines them. function_one in this case.
def function_one(y):
    # Variables defined in a function also belong to that function's local scope.
    z = y + 1

    # Global variables are accessible in every other scope.
    z += x

    print(f'z: {z}, y: {y}, x: {x}')

function_one(20)

# Note that local variables do not leak to global scope.
# These two lines raise errors:
print(y)
print(z)

# Variable shadowing occurs when there are variables in different
# scopes with the same name. Python will use the local version of
# the variable in such cases.
x = 'I am a global variable'
def fun2():
    x = 'I am a local variable'
    print(x) # If no keyword is used, python uses the most local variable

# Note that x has not changed after calling the function
fun2()
print(x)


# Finally, if you want to update a global variable's
# value in python, you must do so explicitly...
def fun3():
    # With this line commented out, the subsequent line throws an error.
    # This is because python thinks we're creating a new LOCAL variable
    # named x. The global keyword tells python we mean to change a global 
    # variable, rather than create a new local variable with the same name.
    # global x
    x += 10

fun3()
