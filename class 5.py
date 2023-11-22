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
        if number_elevator < self.num_bottom or number_elevator > self.elevators:
            print("Error!")
            return

        elevator = self.elevators[number_elevator]
        print(f"The elevator {number_elevator} goes to floor {destination}")
        elevator.go_to_floor(destination)


building = Building(1, 10, 7)
building.run_elevator(1, 8)
