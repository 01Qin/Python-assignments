round_original = 0
while round_original < 5:
    name = input("enter the username: ")
    password = input("Enter the password: ")
    if name == "python" and password == "rules":
        print(f"welcome {name}")
        break
    else:
        print("incorrect username and password, please try again!")
        round_original += 1
    if round_original == 5:
        print("Access denied!")
