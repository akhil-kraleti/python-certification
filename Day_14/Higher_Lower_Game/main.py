import art
import game_data
import random

def compare(a,b):
    if a['follower_count']>b['follower_count']:
        return "a"
    elif a['follower_count']<b['follower_count']:
        return "b"
    return "0"

def check_user_answer(a,b):
    if a==b:
        return True
    else:
        return False


data = game_data.data
is_game_over = False
score = 0

A = random.choice(data)
B = random.choice(data)

print(art.logo)
print(f"Compare A: {A['name']},{A['description']},{A['country']}\n")
print(art.vs+"\n")
print(f"Against B: {B['name']},{B['description']},{B['country']}\n")

while not is_game_over:

    answer = compare(A,B)

    user_answer = input("Enter your answer: ").lower()

    is_correct = check_user_answer(answer,user_answer)

    if is_correct:
        score += 1
        A = B
        B = random.choice(data)
        print("\n"*20)

        print(art.logo)
        print(f"You're right!, Current Score: {score}")
        print(f"Compare A: {A['name']},{A['description']},{A['country']}\n")
        print(art.vs + "\n")
        print(f"Against B: {B['name']},{B['description']},{B['country']}\n")

    else:
        is_game_over = True

print(f"Sorry, That's wrong, Final Score: {score}")

