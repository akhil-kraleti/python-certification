import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
###
choice = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

user_choice = int(input("Type your choice - 0-->Rock, 1-->Paper, 2-->Scissors:"))
computer_choice = random.randint(0,2)



if user_choice > 2:
    print("Invalid Choice, You Lose!")
else:
    print(f"Your choice :\n {choice[user_choice]}\nComputer choice :\n {choice[computer_choice]}")
    if user_choice == computer_choice:
        print("Draw !, Try Again..")
    elif (user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice==2) or (user_choice == 2 and computer_choice ==0):
        print("You Lose!")
    else:
        print("You Win!")