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


while True:
    input_month = input("Please enter a number of a month: ")
    if input_month == "" or input_month == "0":
        break

    input_month = int(input_month)
    input_season = season(input_month)
    print(f"The number of the month is {input_month}, {input_season}.")

print("Input stopped")
