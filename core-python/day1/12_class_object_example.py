# Example 2: Using __init__ to Set Data in a Class

class Dog:
    def __init__(self, name):
        # Store the name inside the object
        self.name = name

    def bark(self):
        # Print a message including the dog's name
        print(f"{self.name} says: Woof! Woof!")

# Create Dog objects with different names
dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

# Call the bark method for each dog
dog1.bark()   # Output: Buddy says: Woof! Woof!
dog2.bark()   # Output: Charlie says: Woof! Woof!

"""
What's new?

- __init__(self, name): This is a constructor. It runs when we create an object.
- self.name = name: It stores the given name inside the object’s data.

Key Point:

- self is used to store data (name) inside the object.
- dog1 has name = "Buddy"; dog2 has name = "Charlie".
"""

# ------------------------ Task ------------------------
# Task: Add new argument 'age' to the Dog class and modify the bark method to include the dog's age in the output.