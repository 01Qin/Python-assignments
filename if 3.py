gender = input("enter the biological gender:")
hemo = float(input("enter the hemoglobin value:"))
if gender == "female":
    if hemo < 117:
        print("A normal hemoglobin value.")
elif 117 >= hemo <= 155:
    print("A low hemoglobin value")
elif hemo > 155:
    print("A high hemoglobin value")
if gender == "male" :
    if hemo < 134:
        print("A normal hemoglobin value.")
elif 134 <= hemo <= 167:
    print("A low hemoglobin value.")
elif hemo > 167:
    print("A low hemoglobin value.")
