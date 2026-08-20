# Procedural way of solving problems
# OOPS Object Oriented Programming System
#  - Tries to solve the complexity of modern day programs
#  - Large teams / numbers of programmers working same codebase
#  - Large codebase
#  - Complex codebase
#  - Trying to organize everything
# Classes, Objects, Inheritance, Polymorphism, Abstraction, Data hiding

# Calculator example
# add, sub etc functions
# operands passing, taking results / sending

class CalculatorV1:

    def add(self, n1, n2):
        print(f"Addition of n1 and n2 is: {n1+n2}")

    def sub(self, n1, n2):
            print(f"Subtraction of n1 and n2 is: {n1-n2}")

# add()

# c is object of class Calculator
c = CalculatorV1()
c.add(1, 2)
c.sub(2, 1)

class Calculator:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(f"Addition of n1 and n2 is: {self.n1+self.n2}")

    def sub(self):
            print(f"Subtraction of n1 and n2 is: {self.n1-self.n2}")

# add()

# c is object of class Calculator
c = Calculator(1, 2)
c.add()
c.sub()

c = Calculator(2, 1)
c.add()
c.sub()