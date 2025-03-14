import math
talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
s_pounds = pounds + talents * 20
s_lots = lots + s_pounds * 32
grams = float(13.3 * float(s_lots))
kilograms = float(grams / 1000)
s_grams = grams % 1000
print(f"The weight in modern units: ")
print(f"{int(kilograms)} kilograms and {s_grams:.2f} grams")
