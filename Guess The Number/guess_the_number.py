import random
import art

#FUNCTIONS
def rand_number():
    value = random.randint(1,100)
    return value

def difficulty_level(difficulty):
    global game_on
    if difficulty == "easy":
        attempts = 10
        return attempts
    elif difficulty == "hard":
        attempts = 5
        return attempts
    else:
        print("Invalid input")
        game_on = False

def compare(number, guess):
    if number == guess:
        print(f"{art.winner}")
        print("You guessed correctly!")
        return False
    if number > guess:
        print("Higher")
        return True
    if number < guess:
        print("Lower")
        return True

#MAIN PROGRAM

print(art.logo)

print("Welcome to the Number Guessing Game!")

game_on = True

while game_on:
    print("I'm thinking of a number between 1 and 100")
    number = rand_number()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = difficulty_level(difficulty)
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0 and game_on:
        guess = int(input("Make a guess: "))
        game_on = compare(number,guess)
        attempts -= 1

    if attempts == 0 and game_on:
        print(f"{art.loser}")
        print(f"You've run out of attempts! The number was {number}.")
        game_on = False

print("Thanks for playing!")