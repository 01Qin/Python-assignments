###################################
def numbers(integers_list):
    even_list = []
    for n in integers_list:
        if n % 2 == 0:
            even_list.append(n)
    return even_list


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8]
    cut_down_list = numbers(original_list)
    print(f"original_list: {original_list}")
    print(f"cut_down_list: {cut_down_list}")
    return


main()


###################################
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

################################
def season(month):
    seasons = ("winter", "spring", "summer", "autumn")

    if month in (12, 1, 2):
        return seasons[0]

    elif month in (3, 4, 5):
        return seasons[1]

    elif month in (6, 7, 8):
        return seasons[2]

    elif month in (9, 10, 11):
        return seasons[3]

    else:
        return 'Invalid month'


input_month = int(input("Please enter a number of a month: "))
input_season = season(input_month)
print(f"The number of the month is {input_month}, {input_season}.")

input_months = []
while True:
    global month
    input_month = input("Please enter a number of a month: ")
    if input_month == "" or input_month == "0":
        break

    input_month = int(input_month)
    input_months.append(input_month)

    for month in input_months:
        input_season = season(month)
    print(f"The number of the month is {month}, {input_season}.")

print("Input stopped")

###################################