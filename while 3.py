import random
num = random.randint(1, 10)
input_num = int(input("Enter a number:"))
while True:
    if input_num > num:
        print(f"Too high", {int(num) - input_num}, "away from", int(num))
        input_num = int(input("Enter a number:"))
    elif input_num < num:
        print(f"Too low", {int(num) - input_num}, "away from", int(num))
        input_num = int(input("Enter a number:"))
    else:
        print("Correct number!")
        break
