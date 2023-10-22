import random


def r_dice():
    return random.randint(1, 6)
def main():
    roll = r_dice()
    while roll != 6:
        print("roll", roll)
        roll = r_dice
    print("roll", roll)


main()
