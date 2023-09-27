number = int(input("Enter a number:"))
while 0 <= number <= 1000:
    if number % 3 == 0:
        print(number)
else:
    print("Execution stopped.")
