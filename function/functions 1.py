round_original = 0
while round_original < 5:
    name = input("Enter the username: ")
    password = input("Enter the password: ")
    if name == "python" and password == "rules":
        print(f"Welcome {name}")
        break
    else:
        print("Incorrect username and password, please try again!")
        round_original += 1
    if round_original == 5:
        print("Access denied!")
