import random

# Generate a random number between 1 and 5
secret_number = random.randint(1, 5)

try:
    # Ask the user for a guess
    guess = int(input("Type a number: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("You won!")
    else:
        print("You lost :c ")

    print(f"The secret number is: {secret_number}")
    
except ValueError:
    print("Please enter a valid integer.")
