# The program should generate a random number between 1 and 10. The user guesses until they get it right.
import random
target_number = random.randint(1, 10)
guess = None
while guess != target_number:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the right number.")