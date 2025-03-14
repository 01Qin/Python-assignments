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
