import shelf

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

class Fade:

    def __init__(self, shelf):
        self.shelf = shelf
        self.direction = 1
        self.index = 1
        self.count = 0
        self.brightness = 200

        shelf.setAll(255,0,0)

    def next(self, curr_tic):
        
        
        if curr_tic % 2 == 0:

            if self.index == 0 and self.direction == 1: # RED UP
                self.shelf.setAll(self.shelf.squares[0].getRed() + 1, self.shelf.squares[0].getGreen(), self.shelf.squares[0].getBlue())
                self.count += 1

                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 2

            elif self.index == 0 and self.direction == 0: # RED DOWN
                self.shelf.setAll(self.shelf.squares[0].getRed() - 1, self.shelf.squares[0].getGreen(), self.shelf.squares[0].getBlue())
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 2

            elif self.index == 1 and self.direction == 1: # GREEN UP
                self.shelf.setAll(self.shelf.squares[0].getRed(), self.shelf.squares[0].getGreen() + 1, self.shelf.squares[0].getBlue())
                self.count += 1


                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 0

            elif self.index == 1 and self.direction == 0: # GREEN DOWN
                self.shelf.setAll(self.shelf.squares[0].getRed(), self.shelf.squares[0].getGreen() - 1, self.shelf.squares[0].getBlue())
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 0

            elif self.index == 2 and self.direction == 1: #BLUE UP
                self.shelf.setAll(self.shelf.squares[0].getRed(), self.shelf.squares[0].getGreen(), self.shelf.squares[0].getBlue() + 1)
                self.count += 1

                if self.count == self.brightness:
                    self.direction = 0
                    self.index = 1

            elif self.index == 2 and self.direction == 0: # BLUE DOWN
                self.shelf.setAll(self.shelf.squares[0].getRed(), self.shelf.squares[0].getGreen(), self.shelf.squares[0].getBlue() - 1)
                self.count -= 1

                if self.count == 0:
                    self.direction = 1
                    self.index = 1

        return self.shelf

            

    