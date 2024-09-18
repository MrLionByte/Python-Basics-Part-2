# Create a Python class Rectangle that represents a rectangle. The class should have the following features :
# Attributes:
# 1: width (float): The width of the rectangle.
# 2: height (float): The height of the rectangle.

# Methods:
# 1: __init__(self, width: float, height: float): Initializes the rectangle with width and height.
# 2: area(self) -> float: Returns the area of the rectangle.
# 3: perimeter(self) -> float: Returns the perimeter of the rectangle.
# 4: __str__(self) -> str: Returns a string representation of the rectangle in the format: "Rectangle(width, height)".

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (self.height+self.width) * 2
    
    def __str__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"
    
shape = Rectangle(5.0,3.0)
print(shape)
print(shape.perimeter())
print(shape.area())


# Create a Python class hierarchy for geometric shapes with the following requirements:

# Base Class: Shape
# Attributes: name (str): The name of the shape.
# Methods:
# __init__(self, name: str): Initializes the shape with its name.
# area(self) -> float: Returns the area of the shape. This should be overridden in derived classes.
# perimeter(self) -> float: Returns the perimeter of the shape. This should be overridden in derived classes.
# __str__(self) -> str: Returns a string representation of the shape, e.g., "Shape(name)".

# Derived Class: Circle
# Attributes: radius (float): The radius of the circle.
# Methods:
# __init__(self, radius: float): Initializes the circle with its radius and sets the name to "Circle".
# area(self) -> float: Returns the area of the circle.
# perimeter(self) -> float: Returns the perimeter of the circle.

# Derived Class: Square
# Attributes: side (float): The length of a side of the square.
# Methods:
# __init__(self, side: float): Initializes the square with its side length and sets the name to "Square".
# area(self) -> float: Returns the area of the square.
# perimeter(self) -> float: Returns the perimeter of the square.

class Shape:
    def __init__(self, name) -> None:
        self.name = name
    
    def area(self):
         raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        return "HOIIIIII "
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self) -> str:
        return f"Shape ({self.name})"


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side: float):
        super().__init__("Square")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

circle = Circle(5.0)
print(circle)            # Output: Shape(Circle)
print(circle.area())     # Output: 78.5
print(circle.perimeter()) # Output: 31.400000000000002

square = Square(4.0)
print(square)            # Output: Shape(Square)
print(square.area())     # Output: 16.0
print(square.perimeter()) # Output: 16.0