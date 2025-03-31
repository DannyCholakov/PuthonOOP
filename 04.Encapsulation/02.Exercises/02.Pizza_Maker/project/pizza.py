from project.dough import Dough
from project.topping import Topping

class Pizza:
    def __init__(self, name: str, dough, max_number_of_toppings: int):
        self.name = name  # Setter validates
        self.dough = dough  # Setter validates
        self.max_number_of_toppings = max_number_of_toppings  # Setter validates
        self.toppings = {}  # Dictionary: topping type -> total weight
        self.__toppings_count = 0  # Counts each addition, even if same topping

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping):
        # Each addition counts toward capacity even if topping already exists.
        if self.__toppings_count >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        self.__toppings_count += 1
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_toppings_weight = sum(self.toppings.values())
        return self.dough.weight + total_toppings_weight
