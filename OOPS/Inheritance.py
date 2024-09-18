class Vehicle: # Parent Class
    def __init__(self,name,edition) -> None: # Constructor
        self.name = name  
        self.edition = edition
    
    def my_vehicle(self): # Method
        return f"{self.name} is build in the year {self.edition}"

class Hyundai(Vehicle): # Single Inheritance from parent to child
    def __init__(self, name, edition,door) -> None:
        super().__init__(name,edition)  # Calls the ParentClass __init__ and passes name and edition to it
        self.door = door
    
    def used_door(self):
        return f"{self.name} has door with {self.door}"
    
v = Hyundai("i-20",2020,"Steel door")
print(v.my_vehicle())
print(v.used_door())

# MRO

class A:
    def i_am(self):
        return "i am A"

class B:
    def i_am(self):
        return "i am B"

class C(B,A):
    def i_am(self):
        return super().i_am()
     
    

c = C
print(A.i_am(c))
print(c.mro())