import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#method one
random_person = random.randint(0,len(friends)-1)
print(friends[random_person])

#method 2
print(random.choice(friends))