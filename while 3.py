import random
num = random.randint(1, 10)
input_num = int(input("enter a number:"))
while True:
    if input_num > num:
        print(f"too high", {int(num) - input_num}, "away from", int(num))
        input_num = int(input("enter a number:"))
    elif input_num < num:
        print(f"too low", {int(num) - input_num}, "away from", int(num))
        input_num = int(input("enter a number:"))
    else:
        print("correct number")
    break
