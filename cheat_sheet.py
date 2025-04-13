# ✅ 1. Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Rex")
print(dog.bark())  # Output: Rex says woof!


# ✅ 2. Inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"


# ✅ 3. Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance


# ✅ 4. Static and Class Methods
class Tool:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        return f"This is {cls.__name__}"


# ✅ 5. Polymorphism and Abstraction
from abc import ABC, abstractmethod

class AnimalAbstract(ABC):
    @abstractmethod
    def sound(self):
        pass

class DogPoly(AnimalAbstract):
    def sound(self):
        return "Woof"


# ✅ 6. SOLID Principles (overview as comments)
# S - Single Responsibility: one class = one responsibility
# O - Open/Closed: open for extension, closed for modification
# L - Liskov Substitution: subclasses can replace base class
# I - Interface Segregation: don't force unused methods
# D - Dependency Inversion: depend on abstractions not concretion


# ✅ 7. Iterators and Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)


# ✅ 8. Decorators
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greet():
    print("Hello")

greet()


# ✅ 9. Testing (unit test example)
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)


# ✅ 10. Design Patterns
# Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory
def get_pet(pet="dog"):
    class Dog: pass
    class Cat: pass
    return Dog() if pet == "dog" else Cat()
