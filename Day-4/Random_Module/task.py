import random
import my_module

# generating random integers in between a,b(including a and b)
# random_integer = random.randint(1,10)
# print(random_integer)

# generating a random float point number between 0.0 and 1.0 (1.0 is not included)
# random_0_to_1 = random.random()
# print(random_0_to_1)

# generating a random float point number between a and b (including a and b)
# random_float = random.uniform(1,10)
# print(random_float)

# print(my_module.my_favorite_number)

#heads or tails with random module
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails==1:
    print("Heads")
else:
    print("Tails")
