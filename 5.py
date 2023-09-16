import math
talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
talents = float(20 * pounds)
pounds = float(32 * lots)
grams = float(13.3 * float(lots))
kilograms = float(grams / 1000)
print(f"The weight in modern units: {kilograms:.2f} kilograms and {grams:.2f} grams")
