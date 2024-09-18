# Abstract Class
# Create an abstract class Vehicle with an abstract method move().
# Then, create two subclasses: Car and Bicycle, each implementing the move() method.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Drive in 4 wheel"

class Bicycle(Vehicle):
    def move(self):
        return "Drive in 2 wheel"


c = Car()
b = Bicycle()
print(c.move(),b.move())

# Interface-Like Behavior
# Define an abstract class Shape with an abstract method draw().
# Implement two concrete classes Triangle and Square that inherit from Shape and provide their own implementation for draw().

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        return "Drawing a triangle with 3 sides"

class Square:
    def draw(self):
        return "Drawing a square  with 4 sides"

T = Triangle()
S =Square()
print(T.draw())
print(S.draw())

