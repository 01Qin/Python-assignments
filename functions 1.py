name = input("Enter the username: ")
password = input("Enter the password: ")
round = 0

while name != "python" and password != "rules":
    name = input("enter the username: ")
    password = input("Enter the password: ")
    round += 1
    if round >= 5:
        print("Access denied!")
        break
else:
    print(f"welcome {name}")
