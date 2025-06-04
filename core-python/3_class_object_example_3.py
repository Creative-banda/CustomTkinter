

# Example : 3. Class with a Simple Method

class Calculator:
    def __init__(self, number):
        self.number = number

    def double(self):
        result = self.number * 2
        print("Double of", self.number, "is", result)

calc = Calculator(5)
calc.double()


"""
Key takeaway:

    self.number stores the number.

    double() uses that data to do something with it.

    self is always the first parameter of any class method to let the method access or modify the object’s own data.

Final Key Point: Why self?

    self is a nickname for the object. You can think of it like:
    
    When you call calc.double(), Python does this:
    
    Calculator.double(calc)
    
    So self is calc here.

"""