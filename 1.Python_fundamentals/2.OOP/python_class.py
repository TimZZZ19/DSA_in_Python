class Car:
    # Constructor (__init__) to initialize attributes
    def __init__(self, make, model, year):
        self.make = make  # Attribute for the car's make (e.g., Toyota)
        self.model = model  # Attribute for the car's model (e.g., Corolla)
        self.year = year  # Attribute for the car's manufacturing year
        self.engine_running = False  # Initially, the engine is off

    # Method to start the engine
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The engine of the {self.make} {self.model} is already running.")

    # Method to stop the engine
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
        else:
            print(f"The engine of the {self.make} {self.model} is already off.")

    # Method to display car info
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


def main():
    # Example usage:

    # Create instances of the Car class
    car1 = Car("Toyota", "Corolla", 2022)
    car2 = Car("Honda", "Civic", 2021)

    # Accessing attributes
    print(f"Car 1 is a {car1.year} {car1.make} {car1.model}")
    print(f"Car 2 is a {car2.year} {car2.make} {car2.model}")

    # Call methods
    car1.display_info()  # Outputs: 2022 Toyota Corolla
    car2.display_info()  # Outputs: 2021 Honda Civic

    car1.start_engine()  # Outputs: The Toyota Corolla's engine has started.
    car2.start_engine()  # Outputs: The Honda Civic's engine has started.
    car2.stop_engine()  # Outputs: The Honda Civic's engine has stopped.
    car2.stop_engine()  # Outputs: The engine of the Honda Civic is already off.


# Run the main method
if __name__ == "__main__":
    main()
