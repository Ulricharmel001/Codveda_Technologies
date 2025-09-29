"""Objectives:
Use the random module to generate a random number.
Give the user multiple attempts to guess the number.
Provide appropriate feedback (e.g.,
"Too high" or "Too low").
Exit the game if the user guesses correctly or after a
maximum number of attempts."""



#pseudocode 
"""START

IMPORT random module

SET secret_number = random integer between 1 and 100
SET max_attempts = 5
SET attempts = 0

REPEAT until attempts = max_attempts
    PROMPT user to enter a guess
    INCREASE attempts by 1

    IF guess equals secret_number
        DISPLAY "Correct! You guessed the number."
        END game
    ELSE IF guess < secret_number
        DISPLAY "Too low"
    ELSE
        DISPLAY "Too high"

IF user did not guess correctly within max_attempts
    DISPLAY "Game over! The number was [secret_number]"

END
"""


import random
attempts = 0
max_attempts = 10
remaining_attempts = max_attempts
while attempts < max_attempts:
    secret_number = random.randint(1, 100)
    print("Remaining Attempts :", remaining_attempts)
    print("Next Secret Number :", secret_number)
    try:
        user_guess = float(input("Enter your number between 1 - 100\n "))
        attempts += 1
        remaining_attempts -= 1 
    except ValueError:
        print("Incorrect Value, enter a number from  1 - 100")
        continue
    print(f"Attempt {attempts} of {max_attempts}.")
    print(f"Remaining attempts: {remaining_attempts}")

    if user_guess == secret_number:
        print("user Guess:", user_guess, " ", "target was number :", secret_number)
        print(f"Congratulations! You guessed the number {secret_number} correctly!")
        print("Game Over! ")
        break
    elif user_guess > 0 and user_guess < secret_number and remaining_attempts > 0:
        print("user Guess:", user_guess, " ", "target number :", secret_number)
        print("Your guess is too low. Try again!")
        continue
    elif user_guess > 0 and user_guess > secret_number and remaining_attempts > 0:
        print("user Guess:", user_guess, " ", "target number :", secret_number)
        print("Your guess is too high. Try again!")
        continue
    elif remaining_attempts == 0:
        print("You’ve used all your attempts. Game over!")
        print(f"The number was {secret_number}. Better luck next time!")
        break
    elif user_guess < 1 or  user_guess > 10 :
        print("You can only guess between 1 and 10")
        continue
    else:
        print("Welcome Here")



