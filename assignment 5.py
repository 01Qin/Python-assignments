##########################

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

#################################

codes = {}
while True:
    new_airport = input("Do you want to enter a new airport,"
                        "fetch the information of an existing airport "
                        "or quit: ")
    if new_airport == "quit":
        print("Execution ends")
        break

    elif new_airport == "enter a new airport":
        ICAO_code = input("Please enter the ICAO code: ")
        airport_name = input("Please enter a name of an airport: ")
        codes[ICAO_code] = airport_name
        print(f"New airport added: {ICAO_code} - {airport_name}")

    elif new_airport == "fetch the information of an existing airport":
        ICAO_code = input("Please enter the ICAO code: ")

        if ICAO_code in codes:
            airport_name = codes[ICAO_code]
            print(f"Airport found: {ICAO_code} - {airport_name}")
        else:
            print("Airport not found.")
    else:
        print("Invalid input. Please try again.")

##################################