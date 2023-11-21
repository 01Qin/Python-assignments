import random


class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        acc_speed = self.current_speed + speed_change
        if acc_speed < 0:
            self.current_speed = 0
        elif acc_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = acc_speed

    def drive(self, hours):
        new_distance = self.current_speed * hours
        self.travelled_distance += new_distance


car_objects = []
for c in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{c}"
    car = Car(registration_number, maximum_speed)
    car_objects.append(car)

race_finished = False
hour = 1

while not race_finished:
    print(f"Hour{hour} of the race: ")
    for car in car_objects:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        print(f"Registration number is: {car.registration_number}.")
        print(f"Maximum speed is: {car.maximum_speed} km/h.")
        print(f"Current speed is: {car.current_speed} km/h.")

        if car.travelled_distance >= 10000:
            race_finished = True
            break
    hour += 1

print("Final results: ")
print("Registration number | Maximum speed | Current speed | Travelled distance")

for car in car_objects:
    print(f"\t\t{car.registration_number}\t\t\t{car.maximum_speed}km/h\t\t\t{car.current_speed}km/h\t\t\t\t{car.travelled_distance}km")
