# While loops are like if statements in that they allow
# you to execute some code based on a condition.
# However, the code in the while statements block will
# repeat until the condition becomes False.
x = 0
while x < 10:
    x += 1
    print(x)

# One common way to use the while loop is to request user
# input until it's valid.
user_in = input("Please type the word 'exit': ")
while user_in != "exit":
    print(f'sorry, you typed {user_in}')
    user_in = input("Please type the word 'exit': ")

# Two keywords, break and continue, can modify the standard looping behavior...

# Normally, this while loop would just run forever (called an infinite loop)
while True:
    x += 1

    if x > 1000000:
        print("x is too big, exiting...")
        break # The break statement exits a loop immediately

print("exited loop.")


# The continue statement allows you to return to the top
# of a loop without reaching the end of that loops block
x = 20
while x > 10:
    x -= 1

    # This operator is called 'modulo' and it returns the remainder
    # of division. So x % 10 == 0 is asking "is x divisible by 10"
    if x % 10 == 0:
        print(f'{x} is divisible by 10')
        continue

    print(f'{x} is not divisible by 10')


# Micro-exercise: use a while loop to compute the sum of all the numbers
# 1 through 100. 