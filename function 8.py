def the_unit_price(diameter, price):
    price_meter = price / (3.14 * ((diameter / 2) ** 2) / 100)
    return round(price_meter, 2)


def main():
    diameter_1 = float(input("Please enter the first diameter: "))
    price_1 = float(input("Please enter the first price: "))
    diameter_2 = float(input("Please enter the second diameter: "))
    price_2 = float(input("Please enter the second price: "))

    unit_price_1 = the_unit_price(diameter_1, price_1)
    unit_price_2 = the_unit_price(diameter_2, price_2)

    if unit_price_2 > unit_price_1:
        print(f"The first pizza is {unit_price_1} euros, provides better value! ")
    elif unit_price_2 < unit_price_1:
        print(f"The second pizza is {unit_price_2} euros, provides better value! ")
    else:
        print("Both pizzas have the same unit price.")


main()
