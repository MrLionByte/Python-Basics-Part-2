# Create a parent class Animal with a method speak() that returns "Animal makes a sound".
# Then create a subclass Dog that overrides the speak() method to return "Dog barks".

class Animal:
    def __init__(self,sound) -> None:
        self.sound = sound

    def speak(self):
        return f"Animal make sound"

class Dog(Animal):
    def __init__(self, sound) -> None:
        super().__init__(sound)
    
    def speak(self):
        return f"Dog barks {self.sound}"

d = Dog("Bow")
print(d.speak())