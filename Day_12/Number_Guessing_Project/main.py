import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function for setting difficulty level
def difficulty_func():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


#Function to check guessed answer against the actual answer
def check_answer(user_guess, actual_answer):
    global attempts
    if user_guess == actual_answer:
        print(f"You got it! The answer was {number}")
        return True
    elif user_guess < actual_answer:
        print(f"Your guess is too low.")
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
            return False
    else:
        print(f"Your guess is too high.")
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
            return False
    return False

Game_over = False

while not Game_over:
    print("\n"*20)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    #Choosing a random number between 1 and 100
    number = random.randint(1, 100)

    attempts = difficulty_func()

    win = False

    #comparing guessed numbers with the actual number
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to gess the number.")
        guess = int(input("Make a guess: "))
        Correct_answer = check_answer(guess, number)
        if Correct_answer:
            win = True
            break

    if not win:
        print("You've run out of guesses, you lose.")
        print("The number I was thinking of was " + str(number))
    if input("Do you want to play again? (y/n): ").lower() == "n":
        Game_over = True



