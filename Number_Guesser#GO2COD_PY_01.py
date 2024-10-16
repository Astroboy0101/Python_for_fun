# GO2COD_PY_01
# By Kena Fayera
import random

def guess_number():
    number = random.randint(1, 100)  # Random number between 1 and 100.
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_number()
