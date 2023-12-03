class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        pass


class Book(Publication):
    def __init__(self, name, author, page_counts):
        super().__init__(name)
        self.author = author
        self.page_counts = page_counts

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_counts}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
compartment_no_6.print_information()
