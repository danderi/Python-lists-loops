# Remember to import random function here
import random
from random import randint
my_list = [4, 5, 734, 43, 45]

# The magic goes below
for i in range(0,10):
    number = random.randint(0,100)
    my_list.append(number)

print(my_list)