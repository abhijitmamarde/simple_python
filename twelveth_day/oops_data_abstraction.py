# Data Abstraction - To restrict the access of private data members and methods

class Point2D_v1:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.calc_quadrant()

    def calc_quadrant(self):
        self.quadrant = "FIRST"
        if self.x >= 0 and self.y < 0:
            self.quadrant = "SECOND"
        elif self.x < 0 and self.y < 0:
            self.quadrant = "THIRD"
    
    def print(self):
        print(f"Point {self.x},{self.y} is in {self.quadrant} quadrant.")

p1 = Point2D_v1()
p2 = Point2D_v1(4, 5)
p3 = Point2D_v1(4, -5)

p3.x = -1
p3.calc_quadrant()

p1.print()
p2.print()
p3.print()


# ====================
class Point2D_v2:

    def __init__(self, x=0, y=0):
        self.update(x, y)

    def __calc_quadrant(self):
        self.__quadrant = "FIRST"
        if self.__x >= 0 and self.__y < 0:
            self.__quadrant = "SECOND"
        elif self.__x < 0 and self.__y < 0:
            self.__quadrant = "THIRD"

    def update(self, x, y):
        self.__x = x
        self.__y = y
        self.__calc_quadrant()
    
    def print(self):
        print(f"Point {self.__x},{self.__y} is in {self.__quadrant} quadrant.")

p1 = Point2D_v2()
p2 = Point2D_v2(4, 5)
p3 = Point2D_v2(4, -5)

p3.__x = -1  # This creates a NEW data member
print("p3.__x =", p3.__x) # --> and could see the value here, but the original __x inside class is not the same. 
# p3.__calc_quadrant()  --> can not be called, it becomes private, could only use inside class 
p3.update(-1, -5)

p1.print()
p2.print()
p3.print()