

# Example : 2. Using __init__ to Set Data

class Dog:
    def __init__(self, name):
        self.name = name  # store the name inside the object
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

dog1.bark() # Output: Buddy says: Woof! Woof!
dog2.bark() # Output: Charlie says: Woof! Woof!




"""
What’s new?

    __init__(self, name): This is a constructor. It runs when we create an object.
    
    self.name = name: It stores the given name inside the object’s data.
    
Key Point:

    self is used to store data (name) inside the object.
    
    dog1 has name = "Buddy"; dog2 has name = "Charlie".
"""

