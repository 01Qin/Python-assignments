import random
num = random.randint(1, 10)
input_num = int(input("enter a number:"))
while input_num != num:
    if input_num > num:
        print(f"too high", {int(num) - input_num})
    else:
        print(f"too low", {int(num) - input_num})
else:
    print("correct number")
    break
