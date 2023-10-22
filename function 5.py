import random


def r_dice():
    roll = random.randint(1, 6)
    return random.randint(1, 6)


def main():
    roll = random.randint(1, 6)
    while roll != 6:
        print("roll:", roll)
        roll = random.randint(1, 6)
    else:
        print("roll:", roll)


main()
