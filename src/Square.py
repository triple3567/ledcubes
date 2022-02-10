class Square:

    def __init__(self, led_list):
        self.led_list = led_list
        self.r = 0
        self.g = 0
        self.b = 0

    def tostring(self):
        return "red = {} green = {} blue = {}".format(self.r, self.g, self.b)

    def getRed(self):
        return self.r

    def getGreen(self):
        return self.g 

    def getBlue(self):
        return self.b   

    def setRed(self, r):
        self.r = r 

    def setGreen(self, g):
        self.g = g 

    def setBlue(self, b):
        self.b = b  

    def setRGB(self, r, g, b):
        self.setRed(r)
        self.setGreen(g)
        self.setBlue(b)