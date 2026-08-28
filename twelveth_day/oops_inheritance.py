class Car:

    def __init__(self, nod=4, tyres=4, capacity=4) -> None:
        self.nod = nod
        self.tyres = tyres
        self.capacity = capacity
        self.color = "White"

    def setColor(self, color):
        self.color = color

    def describe(self):
        print(f"Is a car with {self.color} color, number of doors are: {self.nod}, Total capacity: {self.capacity}, Tyers are: {self.tyres}")

# RedMustangCar is child of Car
# is derived from Car
# is inheriting Car
class RedMustangCar(Car):

    def sportsCarBestSpeed(self):
        print("Can go 0 to 100 ub 8secs...")


class BlueTruck(Car):

    def loadBearingCapacity(self):
        print("1000 ltrs it can take")

c1 = RedMustangCar(nod=2, capacity=2)
c2 = BlueTruck(tyres=12, nod=2, capacity=2)

c1.setColor("Red")
c1.describe()
c1.sportsCarBestSpeed()
# c1.loadBearingCapacity()

c2.setColor("Blue")
c2.describe()
c2.loadBearingCapacity()
# c2.sportsCarBestSpeed()
