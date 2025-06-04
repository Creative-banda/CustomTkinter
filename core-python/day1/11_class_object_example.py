# -----------------------------------------------------------
# Example 1: The Simplest Class and Object in Python
# -----------------------------------------------------------

class Dog:
    def bark(self):
        print("Woof! Woof!")

# Creating an object of the class
dog1 = Dog()
dog1.bark()

# -----------------------------------------------------------
# Explanation:
#   class Dog:
#       Defines a class named 'Dog'.
#
#   def bark(self):
#       A method of the Dog class. 'self' refers to the current object (e.g., dog1).
#
#   dog1 = Dog()
#       Creates an object (instance) of the Dog class.
#
#   dog1.bark()
#       Calls the 'bark' method on the dog1 object.
#
#   What is 'self'?
#       Think of 'self' as the object itself (dog1).
#       When dog1.bark() is called, Python automatically passes dog1 as the first argument to the method.
# -----------------------------------------------------------

# ------------------------ Task ------------------------
# Task: Create a new method in the Dog class called 'sit' that prints "Dog is sitting" and call it using the dog1 object.