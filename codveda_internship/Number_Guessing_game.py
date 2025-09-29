"""Objectives:
Use the random module to generate a random number.
Give the user multiple attempts to guess the number.
Provide appropriate feedback (e.g.,

"Too high" or "Too

low").
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
    secret_number = random.randint(1, 10)
    print("Remaining Attempts :", remaining_attempts)
    print("Next Secret Number :", secret_number)
    try:
        user_guess = float(input("Enter your number between 1 - 10\n "))
        attempts += 1
        remaining_attempts -= 1 
    except ValueError:
        print("Incorrect Value, enter a number from  1 - 10")
        continue

    print("Number of Attempts: ", attempts)
    print('remaining attempt(s) :', remaining_attempts )
    if user_guess == secret_number:
        print("user Guess:", user_guess, " ", "target was number :", secret_number)
        print("Congratulations, you guessed the number")
        print("Game End ")
        break
    elif user_guess < secret_number and remaining_attempts > 0:
        print("user Guess:", user_guess, " ", "target number :", secret_number)
        print("Too Low, Try again!")
        continue
    elif user_guess > secret_number and remaining_attempts > 0:
        print("user Guess:", user_guess, " ", "target number :", secret_number)
        print("Too High, Try again!")
        continue
    elif remaining_attempts == 0:
        print("You have, you have complete all your try ")
        print("Game Over")
        break





