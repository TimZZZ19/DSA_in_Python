class Person:
    # Constructor to initialize the name and age
    def __init__(self, name, age):
        self.name = name  # Person's name
        self.age = age  # Person's age

    # Method to greet the person
    def greet(self):
        print(f"Hello, {self.name}!")

    # Method to check if the person is an adult (18 or older)
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


def main():
    # Create a person object
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 16)

    # Greet the person
    person1.greet()  # Output: Hello, Alice!
    person2.greet()  # Output: Hello, Bob!

    # Check if the person is an adult
    print(
        f"Is {person1.name} an adult? {'Yes' if person1.is_adult() else 'No'}"
    )  # Output: Yes
    print(
        f"Is {person2.name} an adult? {'Yes' if person2.is_adult() else 'No'}"
    )  # Output: No


# This is where the main method is called to run the program
if __name__ == "__main__":
    main()
