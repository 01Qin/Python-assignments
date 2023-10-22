quantity = float(input("enter the quantity of gasoline in gallons: "))


def quantity_gallons(quantity):
    print(f"the quantity of gasoline is: {float(quantity) * 3.785} liters.")


def main():
    volume = float(input("enter the volume of gasoline in gallons: "))
    while volume >= 0:
        print(f"the quantity of gasoline is: {float(volume) * 3.785} liters.")
        volume = float(input("enter the volume of gasoline in gallons: "))
    else:
        print("please enter a positive number!")


quantity_gallons(quantity)


main()
