length = float(input("enter the length of a zander:"))
if length < 42:
    print("release the fish back into the lake")
    print(f"below the size limit the caught fish was: { 42 - length }")
else:
    print("a true zander")
