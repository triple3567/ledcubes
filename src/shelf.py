import square

class Shelf:
    def __init__(self, numsqares):

        self.numsqares = numsqares
        self.squares = []

        for i in range(numsqares):
            self.squares.append(square.Square([(4 * i + 0),(4 * i + 1),(4 * i + 2),(4 * i + 3)]))


    def setAll(self, r, g, b):
        for x in self.squares:
            x.setRGB(r,g,b)

    def setSquare(self, r, g, b, index):
        self.squares[index].setRGB(r,g,b)
