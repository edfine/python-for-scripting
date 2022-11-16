# This function doesn't return anything, but it does print a
# lot of stuff. Before you run this function, predict what it
# will print.

def loops_in_loops():
    c = 0

    for i in range(10):
        for j in range(10):
            print(i, j, c)
            c += 1


loops_in_loops()

def loops_in_loops_comp():
    total = 0
    big = ((i,j,total) for i in range(10) for j in range(10))
    for tup in big:
        print(tup)

loops_in_loops_comp()
# If this result confuses you, simulate its execution by
# manually keeping track of the values in the variables 
# i, j and c as you step through the code line by line.
# Alternately you can examine this code using pythontutor.net

