def converted_to_liters(gallons):
    liters = gallons * 3.785
    return liters


def main():

    while True:
        gallons = float(input("enter the volume of gasoline in gallons: "))
        if gallons < 0:
            break
        print("please enter a positive number!")
        liters = converted_to_liters(gallons)
        print(f"the volume of gasoline in liters: {liters}")


main()
