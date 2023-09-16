import math
talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
pounds = 20 * talents
grams = lots * 13.3
lots = 32 * talents
kilograms = grams / 1000
print(f"The weight in modern units: {kilograms:.2f}kilograms {grams:.2f}grams")
