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
