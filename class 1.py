
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


if __name__ == "main":
    new_car = Car("ABC-123", 142)

    print("All the properties of the new car are:")
    print(f"Registration number is: {new_car.registration_number}.")
    print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
    print(f"Current_speed is: {new_car.current_speed} km/h.")
    print(f"Travelled_distance is: {new_car.travelled_distance} km.")
