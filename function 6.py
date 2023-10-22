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
