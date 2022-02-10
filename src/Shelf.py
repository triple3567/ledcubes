import Square as square
import neopixel
import board

class Shelf:
    def __init__(self):

        s0 = square.Square([62, 63, 64, 65, 66, 67, 68, 69, 70])
        s1 = square.Square([72, 73, 74, 75, 76, 77, 78, 79, 81, 81])
        s2 = square.Square([82, 83, 84, 85, 86, 87, 88, 89, 90, 91])
        s3 = square.Square([61, 60, 59, 58, 57, 56, 55, 54, 54, 52])
        s4 = square.Square([51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41])
        s5 = square.Square([40, 39, 38, 37, 36, 35, 34, 33, 32, 31])
        s6 = square.Square([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        s7 = square.Square([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        s8 = square.Square([21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

        self.numsqares = 9
        self.numLeds = 92
        self.squares = [s0, s1, s2, s3, s4, s5, s6, s7, s8]

        self.neopixel = neopixel.NeoPixel(board.D18, self.numLeds, auto_write=False)


    def update(self):
        for s in self.squares:
            for i in s.led_list:
                self.neopixel[i] = (s.getRed(), s.getGreen(), s.getBlue())
        
        self.neopixel.show()

        return
        
    def setAll(self, r, g, b):

    	for x in self.squares:
            x.setRGB(r,g,b)
        

    def setSquare(self, r, g, b, index):

        self.squares[index].setRGB(r,g,b)
        return

    def setCol(self, r, g, b, index):

        if index == 0:
            self.squares[0].setRGB(r,g,b)
            self.squares[3].setRGB(r,g,b)
            self.squares[6].setRGB(r,g,b)
            
        elif index == 1:
            self.squares[1].setRGB(r,g,b)
            self.squares[4].setRGB(r,g,b)
            self.squares[7].setRGB(r,g,b)
            
        elif index == 2:
            self.squares[2].setRGB(r,g,b)
            self.squares[5].setRGB(r,g,b)
            self.squares[8].setRGB(r,g,b)

        return

    def setRow(self, r, g, b, index):

        if index == 0:
            self.squares[0].setRGB(r,g,b)
            self.squares[1].setRGB(r,g,b)
            self.squares[2].setRGB(r,g,b)
            
        elif index == 1:
            self.squares[3].setRGB(r,g,b)
            self.squares[4].setRGB(r,g,b)
            self.squares[5].setRGB(r,g,b)
            
        elif index == 2:
            self.squares[6].setRGB(r,g,b)
            self.squares[7].setRGB(r,g,b)
            self.squares[8].setRGB(r,g,b)

        return
            


