# Python-Week-5
This is the assignment for Python Week 5

# ACTIVITY 1
Key Features:
1. Encapsulation- attributes like '_brand', '_model' and '_price' are private.

2. Inheritance- 
    1. 'Smartphone' inherits from 'Device'.
    2. 'GamingSmartphone' inherits from 'Smartphone'.

3. Polymorphism-
    1. 'smartphone_info()' is overridden in 'GamingSmartphone'.

4. Dynamic behaviour-
    1. Methods like 'install_app', 'remove_app', and 'toggle_game_mode' alter object state.

# ACTIVITY 2
This code demonstrates polymorphism by defining a 'Vehicle' base class and several subclasses ('Car', 'Plane', 'Boat', and 'Bicycle') that implement the same 'move()' method differently.

Key Features:
1. Base Class ('Vehicle'):
Provides a generic 'move()' method, which can either be overridden by subclasses or used as a default if left unchanged.

2. Subclasses:
Each subclass ('Car', 'Plane', 'Boat', 'Bicycle') overrides the 'move()' method to define how that specific vehicle moves (e.g., "Driving" for 'Car', "Flying" for 'Plane').

3. Polymorphism in Action:
A list of vehicles is created, and the 'move()' method is called on each one. Python determines the correct method to execute based on the object's class, showcasing polymorphism.

4. Output:
Each object prints a unique description of its movement when 'move()' is called.

HAPPY CODING!!!