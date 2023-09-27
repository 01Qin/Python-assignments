number = int(input("Enter a number:"))
while 1 <= number <= 1000:
    if number % 3 == 0:
        break
    print("executing number" + number)
    number = int(input("Enter a number:"))
else:
    print("Execution stopped.")
