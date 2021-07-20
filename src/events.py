import shelf
import math

## TODO
## TIC TAC TOE
## COIN FLIP/ROULETTE, RANDOM BLUE OR ORANGE 18/37, 1/37 for green

class Off:
    def __init__(self, shelf):
        self.shelf = shelf

    def next(self, curr_tic):
        self.shelf.setAll(0,0,0)
        return self.shelf

class StaticOrange:
    def __init__(self, shelf):
        self.shelf = shelf

    def next(self, curr_tic):
        self.shelf.setAll(255,20,0)
        return self.shelf

class StaticWhite:
    def __init__(self, shelf):
        self.shelf = shelf

    def next(self, curr_tic):
        self.shelf.setAll(200,200,200)
        return self.shelf

class BreathingOrange:
    def __init__(self, shelf):
        self.shelf = shelf
        self.xpos = 0
        self.r = 255
        self.g = 20
        self.b = 0

    def next(self, curr_tic):
        self.shelf.setAll(self.func(self.r), self.func(self.g), self.b)
        self.xpos += 1

        if self.xpos > 628300:
            self.xpos = 0

        return self.shelf


    def func(self, val):

        return int(val * (math.cos(self.xpos / 20) + 1) / 2)

class BreathingWhite:
    def __init__(self, shelf):
        self.shelf = shelf
        self.xpos = 0
        self.r = 200
        self.g = 200
        self.b = 200

    def next(self, curr_tic):
        self.shelf.setAll(self.func(self.r), self.func(self.g), self.func(self.b))
        self.xpos += 1

        if self.xpos > 628300:
            self.xpos = 0
            
        return self.shelf


    def func(self, val):

        return int(val * (math.cos(self.xpos / 20) + 1) / 2)

class Fade:

    def __init__(self, shelf):
        self.shelf = shelf
        self.direction = 1
        self.index = 1
        self.count = 0
        self.brightness = 200

        shelf.setAll(200,0,0)

    def next(self, curr_tic):
        
        
        if curr_tic % 2 == 0:

            if self.index == 0 and self.direction == 1: # RED UP
                self.shelf.setAll(self.shelf.squares[0][0].getRed() + 1, self.shelf.squares[0][0].getGreen(), self.shelf.squares[0][0].getBlue())
                self.count += 1

                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 2

            elif self.index == 0 and self.direction == 0: # RED DOWN
                self.shelf.setAll(self.shelf.squares[0][0].getRed() - 1, self.shelf.squares[0][0].getGreen(), self.shelf.squares[0][0].getBlue())
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 2

            elif self.index == 1 and self.direction == 1: # GREEN UP
                self.shelf.setAll(self.shelf.squares[0][0].getRed(), self.shelf.squares[0][0].getGreen() + 1, self.shelf.squares[0][0].getBlue())
                self.count += 1


                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 0

            elif self.index == 1 and self.direction == 0: # GREEN DOWN
                self.shelf.setAll(self.shelf.squares[0][0].getRed(), self.shelf.squares[0][0].getGreen() - 1, self.shelf.squares[0][0].getBlue())
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 0

            elif self.index == 2 and self.direction == 1: #BLUE UP
                self.shelf.setAll(self.shelf.squares[0][0].getRed(), self.shelf.squares[0][0].getGreen(), self.shelf.squares[0][0].getBlue() + 1)
                self.count += 1

                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 1

            elif self.index == 2 and self.direction == 0: # BLUE DOWN
                self.shelf.setAll(self.shelf.squares[0][0].getRed(), self.shelf.squares[0][0].getGreen(), self.shelf.squares[0][0].getBlue() - 1)
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 1

        return self.shelf

            
class Fade2:

    def __init__(self, shelf):
        self.shelf = shelf
        self.direction = 1
        self.index = 1
        self.count = 0
        self.brightness = 200
        self.switch = 0
        self.count = 0

        shelf.setAll(200,0,0)

    def next(self, curr_tic):

        r = self.shelf.squares[0][0].getRed()
        g = self.shelf.squares[0][0].getGreen()
        b = self.shelf.squares[0][0].getBlue()
        
        #event change
        if self.switch == 0:
     
            self.shelf.setAll(r - 1, g + 1, b)
            self.count += 1

            #switch condition
            if self.count == self.brightness:

                self.count = 0
                self.switch = 1



        elif self.switch == 1:

            self.count += 1
            self.shelf.setAll(r, g - 1, b + 1)

            #switch condition
            if self.count == self.brightness:

                self.count = 0
                self.switch = 2

        elif self.switch == 2:

            self.count += 1
            self.shelf.setAll(r, g + 1, b - 1)

            #switch condition
            if self.count == self.brightness:

                self.count = 0
                self.switch = 3

        elif self.switch == 3:
                
            self.count += 1
            self.shelf.setAll(r + 1, g - 1, b)

            #switch condition
            if self.count == self.brightness:

                self.count = 0
                self.switch = 0


        return self.shelf

class Slide:
    
    def __init__(self, shelf):
        
        self.shelf = shelf
        self.index = 1
        self.r = 200
        self.g = 200
        self.b = 200
        self.dir = 0

        self.shelf.setAll(0,0,0)
        self.shelf.setSquare(self.r, self.g, self.b, 0, 0)

    def next(self, curr_tic):

        if curr_tic % 20 == 0:

            if self.index == 0:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 0, 0)

                if self.dir == 0:
                    self.index = 1
                elif self.dir == 1:
                    self.index = 1
                    self.dir = 0

            elif self.index == 1:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 0, 1)

                if self.dir == 0:
                    self.index = 2
                elif self.dir == 1:
                    self.index = 0
            
            elif self.index == 2:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 0, 2)

                if self.dir == 0:
                    self.index = 5
                elif self.dir == 1:
                    self.index = 1
            
            elif self.index == 3:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 1, 0)

                if self.dir == 0:
                    self.index = 6
                elif self.dir == 1:
                    self.index = 4
            
            elif self.index == 4:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 1, 1)

                if self.dir == 0:
                    self.index = 3
                elif self.dir == 1:
                    self.index = 5

            elif self.index == 5:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 1, 2)

                if self.dir == 0:
                    self.index = 4
                elif self.dir == 1:
                    self.index = 2

            elif self.index == 6:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 2, 0)

                if self.dir == 0:
                    self.index = 7
                elif self.dir == 1:
                    self.index = 3

            elif self.index == 7:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 2, 1)

                if self.dir == 0:
                    self.index = 8
                elif self.dir == 1:
                    self.index = 6

            elif self.index == 8:

                self.shelf.setAll(0,0,0)
                self.shelf.setSquare(self.r, self.g, self.b, 2, 2)

                if self.dir == 0:
                    self.index = 7
                    self.dir = 1

        return self.shelf
