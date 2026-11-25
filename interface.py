from abc import ABC, abstractmethod


class VehicleInterface(ABC):

    @abstractmethod
    def process_vehicle(self, wheel: int, engine: str, steering: str) -> bool:
        pass

class Jeep(VehicleInterface):

    def process_vehicle(
        self,
        wheel: int,
        engine: str,
        steering: str
    ) -> bool:

        if wheel <= 0 or not engine or not steering:
            return False

        print("Jeep Vehicle Information")
        print(f"Wheels: {wheel}")
        print(f"Engine: {engine}")
        print(f"Steering: {steering}")

        return True

class Car(VehicleInterface):

    def process_vehicle(
        self,
        wheel: int,
        engine: str,
        steering: str
    ) -> bool:

        if wheel <= 0 or not engine or not steering:
            return False

        print("Car Vehicle Information")
        print(f"Wheels: {wheel}")
        print(f"Engine: {engine}")
        print(f"Steering: {steering}")

        return True

jeep = Jeep()
car = Car()

print(jeep.process_vehicle(4, "Diesel", "Power Steering"))
print(car.process_vehicle(4, "Petrol", "Electric Steering"))
