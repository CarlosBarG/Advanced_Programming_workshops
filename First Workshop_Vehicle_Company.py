class Engine:
    """This class represents the behavior of a vehicle engine."""

    def __init__(self, name, type_motor: str, potency: int, weight: float):
        self.name = name
        self.type_ = type_motor
        self.potency = potency
        self.weight = weight


class Vehicle:
    """
    This class represents the behavior of an abstract class
    to define vehicles.
    """

    def __init__(self, chassis: str, model: str, year: int, engine: Engine):
        if chassis not in ["A", "B"]:
            raise ValueError("This chassis is not valid.")
        
        self.__chassis = chassis
        self.__model = model
        self.__year = year
        self.__gas_consumption = None
        self.__engine = engine

    def _calculate_consumption(self):
        """This method is used to calculate internal gas consumption."""
        consumption = (
            (1.1 * self.__engine.potency)
            + (0.2 * self.__engine.weight)
            - (0.3 if self.__chassis == "A" else 0.5)
        )
        self.__gas_consumption = consumption

    def get_chassis(self) -> str:
        """
        This method is used to get the information of the vehicle's chassis.

        Returns:
        - str: the chassis of the vehicle
        """
        return self.__chassis

    def get_model(self) -> str:
        """
        This method is used to get the information of the vehicle's model.

        Returns:
        - str: the model of the vehicle
        """
        return self.__model

    def get_year(self) -> int:
        """
        This method is used to get the information of the vehicle's year.

        Returns:
        - int: the year of the vehicle
        """
        return self.__year

    def get_gas_consumption(self) -> float:
        """
        This method is used to get the information of the vehicle's gas consumption.

        Returns:
        - float: the gas consumption of the vehicle
        """
        return self.__gas_consumption

    def get_engine(self) -> Engine:
        """
        This method is used to get the information of the vehicle's engine.

        Returns:
        - Engine: the engine of the vehicle
        """
        return self.__engine


class Car(Vehicle):
    """This class is a concrete definition for a Car."""
    def __init__(self, chassis, model, year, engine):
        super().__init__(chassis, model, year, engine)


class Truck(Vehicle):
    """This class is a concrete definition for a truck."""
    def __init__(self, chassis, model, year, engine):
        super().__init__(chassis, model, year, engine)


class Yacht(Vehicle):
    """This class is a concrete definition for a yacht."""
    def __init__(self, chassis, model, year, engine):
        super().__init__(chassis, model, year, engine)


class Motorcycle(Vehicle):
    """This class is a concrete definition for a motorcycle."""
    def __init__(self, chassis, model, year, engine):
        super().__init__(chassis, model, year, engine)


message = """
    Please, choose an option:
    1. Create an engine
    2. Create a car
    3. Create a truck
    4. Create a yacht
    5. Create a motorcycle
    6. Show all engines
    7. Show all vehicles
    8. Exit
"""

engines = {}
vehicles = []

def option_1():
    name = input("Please, write a name to identify the engine:")
    type_motor = input("Please, write the type of engine:")
    potency = int(input("Please, write the potency in an integer value for the engine:"))
    weight = float(input("Please, write the weight in a decimal value for the engine:"))
    new_engine = Engine(name, type_motor, potency, weight)
    engines[name] = new_engine

def create_vehicle(vehicle_type: str):
    engine_name = input(f"Please, write the name of the engine for the {vehicle_type}:")
    model = input(f"Please, write the model for the {vehicle_type}:")
    year = int(input(f"Please, write the year for the {vehicle_type}:"))
    chassis = input(f"Please, write the chassis (A or B) for the {vehicle_type}:")
    engine = engines.get(engine_name)
    if not engine:
        print("Engine not found.")
        return
    if vehicle_type == "car":
        vehicles.append(Car(chassis, model, year, engine))
    elif vehicle_type == "truck":
        vehicles.append(Truck(chassis, model, year, engine))
    elif vehicle_type == "yacht":
        vehicles.append(Yacht(chassis, model, year, engine))
    elif vehicle_type == "motorcycle":
        vehicles.append(Motorcycle(chassis, model, year, engine))

def option_6():
    print("List of engines:")
    for name, engine in engines.items():
        print(f"Name: {name}, Type: {engine.type_}, Potency: {engine.potency}, Weight: {engine.weight}")

def option_7():
    print("List of vehicles:")
    for vehicle in vehicles:
        print(f"Model: {vehicle.get_model()}, Year: {vehicle.get_year()}, Chassis: {vehicle.get_chassis()}, Gas Consumption: {vehicle.get_gas_consumption()}")

def menu():
    """This function represents the menu of the application."""
    print(message)
    option = int(input())
    while option != 8:
        if option == 1:
            option_1()
        elif option == 2:
            create_vehicle("car")
        elif option == 3:
            create_vehicle("truck")
        elif option == 4:
            create_vehicle("yacht")
        elif option == 5:
            create_vehicle("motorcycle")
        elif option == 6:
            option_6()
        elif option == 7:
            option_7()
        else:
            print("Invalid option")
        print(message)
        option = int(input())

if __name__ == "__main__":
    menu()