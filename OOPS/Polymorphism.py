# Create a class Shape with a method area() that returns 0. Then, create subclasses Rectangle and Circle that override the area() method to return the actual area.

class Shape:
    def area(self):
        raise NotImplementedError("This method is must")

class Rectangle(Shape):
    def __init__(self, length, height) -> None:
        self.length = length
        self.height = height
    
    def area(self):
        return self.length*self.height

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(6)
print(c.area())
r = Rectangle(4,2)
print(r.area())

#  Operator Overloading
# Define a class Complex for complex numbers, and overload the + operator to add two complex numbers.
# EX : a+bi
class Complex:
    def __init__(self, real, imaginary) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, Complex):
            real_part = self.real + other.imaginary
            print("Other", other)
            imaginary_part = self.imaginary + other.real
            return Complex(real_part, imaginary_part)
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"
    

c1 = Complex(2, 3) 
c2 = Complex(3, 2) 
c3 = c2 + c1
print(c3)