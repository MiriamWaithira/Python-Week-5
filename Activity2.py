# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

class Bicycle(Vehicle):
    def move(self):
        print("Pedalling")

# Polymorphism in Action
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()