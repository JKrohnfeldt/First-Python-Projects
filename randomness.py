import random

random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)