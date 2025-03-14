import random


class Car:
    def __init__(self, registration_number1, maximum_speed1):
        self.registration_number = registration_number1
        self.maximum_speed = maximum_speed1
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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for a in self.cars:
            speed_change = random.randint(-10, 15)
            a.accelerate(speed_change)
            a.drive(1)

    def print_status(self):
        print("Current status of each car is: ")
        print("Registration number | Maximum speed | Current speed | Travelled distance")

        for b in self.cars:
            print(f"\t\t{b.registration_number}\t\t\t{b.maximum_speed}km/h\t\t\t{b.current_speed}km/h\t\t\t\t{b.travelled_distance}km")

    def race_finished(self):
        for d in self.cars:
            if d.travelled_distance >= self.distance:
                return True
        return False


car_objects = []
for c in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{c}"
    car = Car(registration_number, maximum_speed)
    car_objects.append(car)

race = Race("Grand Demolition Derby", 8000, car_objects)
hour = 1

while not race.race_finished():
    race.hour_passes()
    if hour % 10 == 0:
        race.print_status()
    hour += 1

print("Final results:")
race.print_status()
