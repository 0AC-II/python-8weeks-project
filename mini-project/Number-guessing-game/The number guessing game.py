# The number guessing game

import random

# Welcome message
print("\n🎲 Welcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 10...")
print()

# Create the secret number
secret_number = random.randint(1, 10) 

# Allow the user to guess
for attempt in range(1, 4): 
    guess = int(input("Take a guess: ")) 
    print()
    if guess == secret_number:
        print("✅ Welldone! You guessed correctly in", attempt, "attempt(s) 🎉")
        break  # stop the loop immediately
    elif guess > secret_number:
        print("Oops, too high! Guess lower. You have", 3 - attempt, "attempts left")
    else: 
        print("Oops, too low! Guess higher. You have", 3 - attempt, "attempts left")

else:  
    # This `else` runs only if the for-loop completes WITHOUT a break
    print("\n❌ Sorry, Game Over. You have exhausted your attempts") 
    print("\nThe Secret number was:", secret_number)
    print("\nBetter luck next time!")
