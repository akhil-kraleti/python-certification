import random
from hangman_words import word_list as word_list
from hangman_art import stages as stages
from hangman_art import logo as logo

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
print(logo)

choosen_word = random.choice(word_list)

letter_count = len(choosen_word)

placeholder = ""



game_over = False

correct_letters = []
Guessed_letters_list = []

remaining_chances = 6

print("You have 6 chances")
print(stages[6])

while letter_count>0:
    placeholder += "_"
    letter_count -= 1
print(placeholder)

while not game_over:
    Guessed_letter = input("Guess the letter: ").lower()



    display = ""

    if (Guessed_letter in correct_letters) or (Guessed_letter in Guessed_letters_list):
        print("You have already guessed this letter\nTry again")
        continue

    if Guessed_letter not in Guessed_letters_list:
        Guessed_letters_list.append(Guessed_letter)


    for letter in choosen_word :

        if letter == Guessed_letter:
             display += letter
             correct_letters.append(Guessed_letter)

        elif letter in correct_letters:
            display += letter
        else:
            display  += "_"

    print(display)
    if Guessed_letter not in choosen_word:
        remaining_chances -= 1

    print(stages[remaining_chances])
    print(f"You have {remaining_chances} chances left")

    if remaining_chances == 0:
        print("****************************************** You Lose! ******************************************")
        print(f"The word was '{choosen_word}'")
        game_over = True

    if "_" not in display:
        game_over = True
        print("****************************************** You Win! ******************************************")