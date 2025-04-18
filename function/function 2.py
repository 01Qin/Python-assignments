import random
number = int(input("How many dice do you want to roll: "))
number_sum = 0

for r in range(number):
    roll = random.randint(1,6)
    number_sum += roll
    print(f"The sum of the rolls is {number_sum}.")
