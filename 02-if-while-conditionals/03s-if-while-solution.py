import random

secret_number = random.randint(1, 100)
number_of_guesses = 0

while True:
    print(f'\nYou have {10 - number_of_guesses} guesses remaining.')
    current_guess = input("Guess a number: ")

    # Check if the value can be coerced to an integer.
    if not current_guess.isnumeric():
        print(f'You guessed {current_guess}, which is not an integer. Try again.')
        continue

    # Coerce the guess to an integer.
    current_guess = int(current_guess)

    # Increment the number of number guesses.
    number_of_guesses += 1

    if current_guess == secret_number:
        print("Congratulations, you guessed it!")
        break
    elif number_of_guesses == 10:
        print("Unfortunately, you have run out of guesses. The number was {secret_number}.")
        break
    elif current_guess < secret_number:
        print(f'Your guess ({current_guess}) is smaller than the number I chose.')
    elif current_guess > secret_number:
        print(f'Your guess ({current_guess}) is larger than the number I chose.')

print("I had fun, thanks for playing.")