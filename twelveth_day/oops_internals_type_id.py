class Calculator:

    def __init__(self, n1, n2):
        # Data memebers
        # Methods - add and sub
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print("Type of self is:", type(self))
        print("Address of self is:", id(self))
        print("Type of self.n1 is:", type(self.n1))
        print(f"Addition of n1 and n2 is: {self.n1+self.n2}")

    def sub(self):
        print(f"Subtraction of n1 and n2 is: {self.n1-self.n2}")

# add()

# c is object of class Calculator
c = Calculator(1, 2)
c.add()
print("c n1 is", c.n1)

c2 = Calculator(1, 2)
c2.add()
print("c2 n1 is", c2.n1)

c3 = Calculator(1, 2)
c3.add()
print("c3 n1 is", c3.n1)

if c == c3:
    print("Same")
else:
    print("Not Same")

if (c.n1 == c3.n1) and (c.n2 == c3.n2):
    print("Values Same")
else:
    print("Values Not Same")