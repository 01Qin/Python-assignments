###################
round_original = 0
while round_original < 5:
    name = input("Enter the username: ")
    password = input("Enter the password: ")
    if name == "python" and password == "rules":
        print(f"Welcome {name}")
        break
    else:
        print("Incorrect username and password, please try again!")
        round_original += 1
    if round_original == 5:
        print("Access denied!")


#########################
import random
number = int(input("How many dice do you want to roll: "))
number_sum = 0
for r in range(number):
    roll = random.randint(1,6)
    number_sum += roll
    print(f"The sum of the rolls is {number_sum}.")



##############################
numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(float(number))
sorted_numbers = sorted(numbers, reverse=True)
five_numbers = sorted_numbers[:5]
print("The five greatest numbers in descending order:")
for n in five_numbers:
    print(f"The five greatest number are {n}.")


####################################
cities = []
for d in range(5):
    input_city = input("Enter a city: ")
    cities.append(input_city)
for c in cities:
    print(c)


##############################
import random


def r_dice():
    roll = random.randint(1, 6)
    return random.randint(1, 6)


def main():
    roll = random.randint(1, 6)
    while roll != 6:
        print("Roll:", roll)
        roll = random.randint(1, 6)
    else:
        print("Roll:", roll)


main()


##########################################
def converted_to_liters(gallons):
    liters = gallons * 3.785
    return liters


def main():

    while True:
        gallons = float(input("Enter the volume of gasoline in gallons: "))
        if gallons < 0:
            print("Please enter a positive number!")
            break

        liters = converted_to_liters(gallons)
        print(f"The volume of gasoline in liters: {liters}")


main()
#############################