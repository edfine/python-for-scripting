# The assert statement is a way to throw an error if a boolean expression \
# evaluates to false.

# Running this will be fine
assert True

# Running this code will raise an error. 
# (comment it out to run the rest of this file)
assert False

# Asserts can be used to check conditions that should always be true
# For example, a function that requires numerical input in order to
# work properly might look like this:
def summation(array):
    sum = 0
    for num in array:
        assert isinstance(num, (int, float))
        sum += num
    
    return sum

# Works just fine
summation([1, 2, 3])

# Errors out
summation([1, 2, 'g'])

# Assertions can also be used as a very basic way to test code.
# There are much more robust frameworks for testing code effectively
# but there is a lot of overhead that makes using them challenging for
# beginners. 

# Here's an example of testing with assert:

assert summation([]) == 0
assert summation([1, 1, 1]) == 3
assert summation([2, -3]) == -1
# ... And so on ...
print("all tests passed")