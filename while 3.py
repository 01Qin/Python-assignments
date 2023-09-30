import random
num = random.randint[1-10]
input_num = int(input("enter a number:"))
wrong_num = int(num) - input_num
while input_num != num:
    if wrong_num > 0:
        print(f"too high",{int(num) - input_num})
    else:
        print(f"too low",{int(num) - input_num})
else:
    print("correct number")


