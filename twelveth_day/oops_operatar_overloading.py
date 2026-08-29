class Point2D:

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

    def add(self, p2):
        return Point2D(self.__x + p2.__x, self.__y + p2.__y)

    def __add__(self, p2):
        return self.add(p2)

    def __sub__(self, p2):
        return self.add(p2)

p1 = Point2D(1, 2)
p2 = Point2D(3, 5)

# TypeError: unsupported operand type(s) for +: 'Point2D' and 'Point2D'
# p3 = p1 + p2
# p3 = p1.add(p2)
# p3 = Point2D(4, 7)

p3 = p1 - p2
# p3 = Point2D(-2, -3)  # -- This should be the answer, ASSIGNMENT

p1.print()
p2.print()
p3.print()