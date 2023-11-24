###########################################################
class Car:
    def __init__(self, registration_number, maximum_speed):
        self._registration_number = registration_number
        self._maximum_speed = maximum_speed
        self._current_speed = 0
        self._travelled_distance = 0

    def accelerate(self, speed_change):
        acc_speed = self._current_speed + speed_change
        if acc_speed < 0:
            self._current_speed = 0
        elif acc_speed > self._maximum_speed:
            self._current_speed = self._maximum_speed
        else:
            self._current_speed = acc_speed

    def drive(self, hours):
        new_distance = self._current_speed * hours
        self._travelled_distance += new_distance

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def travelled_distance(self):
        return self._travelled_distance


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("All the properties of the new car are:")
print(f"Registration number is: {new_car.registration_number}.")
print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
print(f"Current speed is: {new_car.current_speed} km/h.")

new_car.accelerate(-200)
print(f"Final speed is: {new_car.current_speed} km/h.")

####################################################################

class Car:
    def __init__(self, registration_number, maximum_speed):
        self._registration_number = str(registration_number)
        self._maximum_speed = float(maximum_speed)
        self._current_speed = 0.0
        self._travelled_distance = 0.0

    def accelerate(self, speed_change):
        acc_speed = self._current_speed + speed_change
        if acc_speed < 0:
            self._current_speed = 0
        elif acc_speed > self._maximum_speed:
            self._current_speed = self._maximum_speed
        else:
            self._current_speed = acc_speed

    def drive(self, hours):
        new_distance = self._current_speed * hours
        self._travelled_distance += new_distance

    def stop(self):
        self._current_speed = 0

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def travelled_distance(self):
        return self._travelled_distance


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("All the properties of the new car are:")
print(f"Registration number is: {new_car.registration_number}.")
print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
print(f"Current speed is: {new_car.current_speed} km/h.")

new_car.accelerate(-200)
print(f"Final speed is: {new_car.current_speed} km/h.")

new_car.drive(1.5)
print(f"Travelled distance is: {new_car.travelled_distance} km.")

#################################################################

import random


class Car:

    def __init__(self, registration_number1, maximum_speed1):
        self.registration_number1 = registration_number1
        self.maximum_speed1 = maximum_speed1
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change1):
        acc_speed = self.current_speed + speed_change1
        if acc_speed < 0:
            self.current_speed = 0
        elif acc_speed > self.maximum_speed1:
            self.current_speed = self.maximum_speed1
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
        print(f"Registration number is: {car.registration_number1}.")
        print(f"Maximum speed is: {car.maximum_speed1} km/h.")
        print(f"Current speed is: {car.current_speed} km/h.")

        if car.travelled_distance >= 10000:
            race_finished = True
            break
    hour += 1

print("Final results: ")
print("Registration number | Maximum speed | Current speed | Travelled distance")

for car in car_objects:
    print(f"\t\t{car.registration_number1}\t\t\t{car.maximum_speed1}km/h\t\t\t{car.current_speed}km/h\t\t\t\t{car.travelled_distance}km")

#################################################################

class Elevator:
    def __init__(self, numbers_top, numbers_bottom):
        self. numbers_top = numbers_top
        self.numbers_bottom = numbers_bottom
        self.new_elevator = numbers_bottom

    def go_to_floor(self, floor):
        if floor < self.numbers_bottom or floor > self. numbers_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The new elevator is now on floor {floor}.")

    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
        print(f"The elevator is now on floor {self.new_elevator}.")

    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
        print(f"The elevator is now on floor {self.new_elevator}.")


elevator = Elevator(10, 1)
elevator.go_to_floor(4)
elevator.go_to_floor(elevator.numbers_bottom)

###################################################

class Elevator:
    def __init__(self, numbers_bottom, numbers_top):
        self.numbers_bottom = numbers_bottom
        self.numbers_top = numbers_top
        self.new_elevator = numbers_bottom

    def go_to_floor(self, floor):
        if floor < self.numbers_bottom or floor > self.numbers_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The new elevator is now on floor {floor}.")

    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
        print(f"The elevator is now on floor {self.new_elevator}.")

    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
        print(f"The elevator is now on floor {self.new_elevator}.")


class Building:
    def __init__(self, num_bottom, num_top, num_elevators):
        self.num_bottom = num_bottom
        self.num_top = num_top
        self.num_elevators = num_elevators
        self.elevators = []
        for e in range(num_elevators):
            elevator = Elevator(num_bottom, num_top)
            self.elevators.append(elevator)

    def run_elevator(self, number_elevator, destination):
        if number_elevator < 0 or number_elevator >= self.num_elevators:
            print("Error!")
            return

        elevator = self.elevators[number_elevator]
        print(f"The elevator {number_elevator} goes to floor {destination}.")
        elevator.go_to_floor(destination)


building = Building(1, 10, 7)
building.run_elevator(1, 8)

#####################################################

class Elevator:
    def __init__(self, num_bottom, num_top):
        self. num_top = num_top
        self.num_bottom = num_bottom
        self.new_elevator = num_bottom

    def go_to_floor(self, floor):
        if floor < self.num_bottom or floor > self.num_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The new elevator is now on floor {floor}.")

    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
        print(f"The elevator is now on floor {self.new_elevator}.")

    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
        print(f"The elevator is now on floor {self.new_elevator}.")


class Building:
    def __init__(self, num_bottom, num_top, num_elevators):
        self.num_bottom = num_bottom
        self.num_top = num_top
        self.num_elevators = num_elevators
        self.elevators = []
        for _ in range(num_elevators):
            elevator = Elevator(num_bottom, num_top)
            self.elevators.append(elevator)

    def run_elevator(self, number_elevator, destination):
        if number_elevator < 0 or number_elevator >= self.num_elevators:
            print("Error!")
            return

        elevator = self.elevators[number_elevator]
        print(f"The elevator {number_elevator} goes to floor {destination}")
        elevator.go_to_floor(destination)

    def fire_alarm(self):
        print("Fire alarm activated!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.num_bottom)


building = Building(1, 10, 7)
building.run_elevator(1, 8)
building.fire_alarm()

######################################################

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

##############################################




