names = set()
while True:
    input_name = input("Please enter a name: ")
    if input_name == "":
        print("Invalid name")
        break
    elif input_name in names:
        print("Existing name")
    else:
        print("New name")

    names.add(input_name)

print("List of names:")
for n in names:
    print(n)
