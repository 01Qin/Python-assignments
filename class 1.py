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

new_car.drive(1.5)
print(f"Travelled distance is: {new_car.travelled_distance} km.")
