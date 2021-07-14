import square

class Shelf:
    def __init__(self, numsqares):

        s0 = square.Square([0, 1, 2, 3, 4, 5, 6, 7, 8])
        s1 = square.Square([9, 10, 11, 12, 13, 14, 15, 16, 17])
        s2 = square.Square([18, 19, 20, 21, 22, 23, 24, 25, 26])
        s3 = square.Square([27, 28, 29, 30, 31, 32, 33, 34, 35])
        s4 = square.Square([36, 37, 38, 39, 40, 41, 42, 43, 44])
        s5 = square.Square([45, 46, 47, 48, 49, 50, 51, 52, 53])
        s6 = square.Square([54, 55, 56, 57, 58, 59, 60, 61, 62])
        s7 = square.Square([63, 64, 65, 66, 67, 68, 69, 70, 71])
        s8 = square.Square([72, 73, 74, 75, 76, 77, 78, 79, 80])

        self.numsqares = numsqares
        self.squares = [[s0, s1, s2], [s3, s4, s5], [s6, s7, s8]]

        


    def setAll(self, r, g, b):
        for col in self.squares:
            for x in col:
                x.setRGB(r,g,b)

    def setSquare(self, r, g, b, row, col):
        self.squares[row][col].setRGB(r,g,b)
