def the_unit_price(diameter, price):
    price_meter = price / ((diameter / 2) ** 2 * 3.14 / 100)
    return r(price_meter,2)


def main():
    diameter_1 = float(input("please enter the first diameter: "))
    price_1 = float(input("please enter the first price: "))
    diameter_2 = float(input("please enter the second diameter: "))
    price_2 = float(input("please enter the second price: "))

    unit_price_1 = the_unit_price(diameter_1, price_1)
    unit_price_2 = the_unit_price(diameter_2, price_2)

    if unit_price_2 > unit_price_1:
        print(f"the first pizza is {unit_price_1}, provides better value! ")
    else:
        print(f"the second pizza is{unit_price_2}, provides better value! ")


main()
