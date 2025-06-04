

# Example : 1 The Simplest Class and Object
class Dog:
    def bark(self):
        print("Woof! Woof!")

# Creating an object of the class
dog1 = Dog()
dog1.bark()




"""
Explanation:
    class Dog: defines a class named Dog.

    def bark(self): is a method. self refers to the current object (dog1).

    dog1 = Dog() creates an object of Dog.

    dog1.bark() calls the method bark() on the object.

    What is self?
    Think of self as the object itself (dog1). When dog1.bark() is called, Python automatically sends dog1 as the first argument to the method.
"""
