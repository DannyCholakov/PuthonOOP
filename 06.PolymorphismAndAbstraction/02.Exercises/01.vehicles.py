from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION) * distance
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION) * distance
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95