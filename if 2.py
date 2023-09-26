c = str(input("enter the cabin class of a cruise ship:"))
if c == "LUX":
    print("upper-deck cabin with a balcony.")
elif c == "A":
    print("above the car deck, equipped with a window.")
elif c == "B":
    print("windowless cabin above the car deck.")
elif c == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
