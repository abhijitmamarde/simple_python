from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, piece_color) -> None:
        self.piece_color = piece_color

    @abstractmethod
    def move(self):
        pass

    def tellColor(self):
        print(f"This is an piece for {self.piece_color} player")

class Horse(Piece):

    def move(self):
        print("Moving 2 accross and 1 Sideways")

class Bishop(Piece):

    def __init__(self, piece_color, color) -> None:
        self.piece_color = piece_color
        self.color=color
    
    def move(self):
        print(f"Moving diagonally in {self.color} squares")

class Rook(Piece):

    def move(self):
        print("Moving straight or sideways squares")

p1 = Horse("White")
p2 = Bishop("Black", "White")
p3 = Bishop("Black", "Black")

p1.move()
p1.tellColor()

p2.move()
p2.tellColor()

p3.move()
p3.tellColor()

p4 = Rook("Black")
p4.move()
