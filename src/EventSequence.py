import threading
import Shelf as shelf
import math
import time
import requests, json

class EventSequence(threading.Thread):
    def __init__(self):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.shelf = shelf.Shelf()
        self.stopFlag = False


    def run(self):
        self.shelf.setAll(255,255,255)
        self.shelf.update()

    def stop(self):
        self.stopFlag = True

    def checkStopFlag(self):
        return self.stopFlag
        

class Off(EventSequence):

    def __init__(self):
        super().__init__()
        
    
    def run(self):
        self.shelf.setAll(0, 0, 0)
        self.shelf.update()

class ColorSelect(EventSequence):

    def __init__(self,colorTuple):
        super().__init__()
        self.r = colorTuple.red
        self.g = colorTuple.green
        self.b = colorTuple.blue

    
    def run(self):
        self.shelf.setAll(self.r, self.g, self.b)
        self.shelf.update()

class Fade(EventSequence):
    
    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0

    def stepRed(self,tick):
        self.r = int((math.sin((tick/1000)+0) + 1)*127.5)

    def stepGreen(self,tick):
        self.g = int((math.sin((tick/1000)+(2*math.pi/3))+1)*127.5)

    def stepBlue(self,tick):
        self.b = int((math.sin((tick/1000)+(4*math.pi/3))+1)*127.5)

    def step(self, tick):
        self.stepRed(tick)
        self.stepGreen(tick)
        self.stepBlue(tick)
    
    def run(self):
        tick = 2000

        while True:
            self.step(tick)
            self.shelf.setAll(self.r, self.g, self.b)
            self.shelf.update()
            tick += 1

            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

class Circle(EventSequence):

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        
    def stepRed(self,tick):
        self.r = int((math.sin((tick/20)+0) + 1)*127.5)

    def stepGreen(self,tick):
        self.g = int((math.sin((tick/20)+(2*math.pi/3))+1)*127.5)

    def stepBlue(self,tick):
        self.b = int((math.sin((tick/20)+(4*math.pi/3))+1)*127.5)

    def step(self, tick):
        self.stepRed(tick)
        self.stepGreen(tick)
        self.stepBlue(tick)

    def run(self):

        tick = 40
        while True:

            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break


            self.shelf.setSquare(0, 0, 0, 7)
            self.shelf.setSquare(0, 0, 0, 6)
            self.shelf.setSquare(0, 0, 0, 3)
            self.step(tick)
            self.shelf.setCol(self.r, self.g, self.b, 0)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 0)
            self.step(tick)
            self.shelf.setSquare(self.r, self.g, self.b, 3)
            self.shelf.setSquare(self.r, self.g, self.b, 0)
            self.shelf.setSquare(self.r, self.g, self.b, 1)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setSquare(0, 0, 0, 3)
            self.shelf.setSquare(0, 0, 0, 0)
            self.shelf.setSquare(0, 0, 0, 1)
            self.step(tick)
            self.shelf.setRow(self.r, self.g, self.b, 0)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 0)
            self.step(tick)
            self.shelf.setSquare(self.r, self.g, self.b, 1)
            self.shelf.setSquare(self.r, self.g, self.b, 2)
            self.shelf.setSquare(self.r, self.g, self.b, 5)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setSquare(0, 0, 0, 1)
            self.shelf.setSquare(0, 0, 0, 2)
            self.shelf.setSquare(0, 0, 0, 5)
            self.step(tick)
            self.shelf.setCol(self.r, self.g, self.b, 2)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 2)
            self.step(tick)
            self.shelf.setSquare(self.r, self.g, self.b, 5)
            self.shelf.setSquare(self.r, self.g, self.b, 8)
            self.shelf.setSquare(self.r, self.g, self.b, 7)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setSquare(0, 0, 0, 5)
            self.shelf.setSquare(0, 0, 0, 8)
            self.shelf.setSquare(0, 0, 0, 7)
            self.step(tick)
            self.shelf.setRow(self.r, self.g, self.b, 2)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 2)
            self.step(tick)
            self.shelf.setSquare(self.r, self.g, self.b, 7)
            self.shelf.setSquare(self.r, self.g, self.b, 6)
            self.shelf.setSquare(self.r, self.g, self.b, 3)
            self.shelf.update()

            tick += 1
            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

class Bounce(EventSequence):
    
    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0

    def stepRed(self,tick):
        self.r = int((math.sin((tick/10)+0) + 1)*127.5)

    def stepGreen(self,tick):
        self.g = int((math.sin((tick/10)+(2*math.pi/3))+1)*127.5)

    def stepBlue(self,tick):
        self.b = int((math.sin((tick/10)+(4*math.pi/3))+1)*127.5)

    def step(self, tick):
        self.stepRed(tick)
        self.stepGreen(tick)
        self.stepBlue(tick)
    
    def run(self):
        tick = 20

        while True:
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.step(tick)
            
            self.shelf.setRow(0, 0, 0, 0)
            self.shelf.setCol(self.r, self.g, self.b, 0)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 0)
            self.shelf.setCol(self.r, self.g, self.b, 1)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 1)
            self.shelf.setCol(self.r, self.g, self.b, 2)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 2)
            self.shelf.setRow(self.r, self.g, self.b, 0)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 0)
            self.shelf.setRow(self.r, self.g, self.b, 1)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 1)
            self.shelf.setRow(self.r, self.g, self.b, 2)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 2)
            self.shelf.setCol(self.r, self.g, self.b, 2)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 2)
            self.shelf.setCol(self.r, self.g, self.b, 1)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 1)
            self.shelf.setCol(self.r, self.g, self.b, 0)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setCol(0, 0, 0, 0)
            self.shelf.setRow(self.r, self.g, self.b, 2)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 2)
            self.shelf.setRow(self.r, self.g, self.b, 1)
            self.shelf.update()

            time.sleep(0.5)
            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break

            self.shelf.setRow(0, 0, 0, 1)
            self.shelf.setRow(self.r, self.g, self.b, 0)
            self.shelf.update()

            time.sleep(0.5)


            tick += 1

class Weather(EventSequence):

    def __init__(self):
        super().__init__()

        self.apiKey = '8870dde0777b119770d32a4e49ed592c'
        self.baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
        self.cityName = 'Gainesville'
        self.units = 'imperial'
        self.r = 0
        self.g = 0
        self.b = 0
        
        completeUrl = self.baseUrl + "appid=" + self.apiKey + "&q=" + self.cityName + "&units=" + self.units
        response = requests.get(completeUrl)
        x = response.json()
        if x["cod"] != "404":

            self.weatherId = x['weather'][0]['id']
            self.currentTemperatureFeelsLike = float(x['main']["feels_like"])
            print(str(self.currentTemperatureFeelsLike) + " " + x['weather'][0]['description'])
            temp = str(self.weatherId)
            self.weatherId = int(temp[0])

        if self.currentTemperatureFeelsLike > 80.0:
            self.r = 255
            self.g = 0
            self.b = 0
        elif self.currentTemperatureFeelsLike > 65.0:
            self.r = 255
            self.g = 64
            self.b = 0
        elif self.currentTemperatureFeelsLike > 45.0:
            self.r = 255
            self.g = 97
            self.b = 11
        elif self.currentTemperatureFeelsLike > 25:
            self.r = 105
            self.g = 105
            self.b = 230
        else:
            self.r = 0
            self.g = 0
            self.b = 128

        

    
    def run(self):
        
        self.shelf.setAll(self.r, self.g, self.b)
        self.shelf.update()

        tick = 0
        drizzleIndex = 8
        rainIndex = 14
        

        while True:
            self.shelf.setAll(self.r, self.g, self.b)

            #Thunderstorm
            if self.weatherId == 2:
                if tick % 6 == 0:
                    self.shelf.setRow(0, 139, 139, 0)
                    self.shelf.update()
                    time.sleep(0.2)

                    self.shelf.setRow(self.r, self.g, self.b, 0)
                    self.shelf.setRow(0, 139, 139, 1)
                    self.shelf.update()
                    time.sleep(0.2)

                    self.shelf.setRow(self.r, self.g, self.b, 1)
                    self.shelf.setRow(0, 139, 139, 2)
                    self.shelf.update()
                    time.sleep(0.2)

                    self.shelf.setAll(self.r, self.g, self.b)
            #Drizzle
            elif self.weatherId == 3:
                    
                drizzleOrder = [0,3,6,1,4,7,2,5,8]

                self.shelf.setSquare(self.r, self.g, self.b, drizzleOrder[drizzleIndex])

                drizzleIndex = (drizzleIndex + 1) % 9

                self.shelf.setSquare(0, 139, 139, drizzleOrder[drizzleIndex])
            #Rain
            elif self.weatherId == 5:

                RainOrder = [[-1,0], [0, 3], [3,6], [-1,6], [-1, -1 ], [-1, 1], [1, 4], [4, 7], [7, -1], [-1, -1], [-1, 2], [2, 5], [5, 8], [8, -1], [-1, -1]]

                self.shelf.setSquare(self.r, self.g, self.b, RainOrder[rainIndex][0])
                self.shelf.setSquare(self.r, self.g, self.b, RainOrder[rainIndex][1])

                rainIndex = (rainIndex + 1) % 15

                self.shelf.setSquare(0, 139, 139, RainOrder[rainIndex][0])
                self.shelf.setSquare(0, 139, 139, RainOrder[rainIndex][1])
                
            #Snow
            elif self.weatherId == 6:
                if tick % 5 == 0:
                    snowR = 205
                    snowG = 201
                    snowB = 201

                    for i in range(100):

                        newR = int((self.r * ((100.0 - i) / 100.0)) + (snowR * (i / 100.0)))
                        newG = int((self.g * ((100.0 - i) / 100.0)) + (snowG * (i / 100.0)))
                        newB = int((self.b * ((100.0 - i) / 100.0)) + (snowB * (i / 100.0)))

                        self.shelf.setSquare(newR, newG, newB, 0)
                        self.shelf.setSquare(newR, newG, newB, 2)
                        self.shelf.setSquare(newR, newG, newB, 4)
                        self.shelf.setSquare(newR, newG, newB, 6)
                        self.shelf.setSquare(newR, newG, newB, 8)
                        self.shelf.update()

                        if self.checkStopFlag():
                            self.shelf.setAll(0, 0, 0)
                            self.shelf.update()
                            break

                        time.sleep(.005)

                    for i in range(100):
                        newR = int((snowR * ((100.0 - i) / 100.0)) + (self.r * (i / 100.0)))
                        newG = int((snowG * ((100.0 - i) / 100.0)) + (self.g * (i / 100.0)))
                        newB = int((snowB * ((100.0 - i) / 100.0)) + (self.b * (i / 100.0)))

                        self.shelf.setSquare(newR, newG, newB, 0)
                        self.shelf.setSquare(newR, newG, newB, 2)
                        self.shelf.setSquare(newR, newG, newB, 4)
                        self.shelf.setSquare(newR, newG, newB, 6)
                        self.shelf.setSquare(newR, newG, newB, 8)
                        self.shelf.update()

                        if self.checkStopFlag():
                            self.shelf.setAll(0, 0, 0)
                            self.shelf.update()
                            break

                        time.sleep(.005)

            #Atmosphere (Hazy)
            elif self.weatherId == 7:
                if tick % 5 == 0:
                    hazeR = 205
                    hazeG = 201
                    hazeB = 201

                    for i in range(100):

                        newR = int((self.r * ((100.0 - i) / 100.0)) + (hazeR * (i / 100.0)))
                        newG = int((self.g * ((100.0 - i) / 100.0)) + (hazeG * (i / 100.0)))
                        newB = int((self.b * ((100.0 - i) / 100.0)) + (hazeB * (i / 100.0)))

                        self.shelf.setAll(newR, newG, newB)

                        self.shelf.update()

                        if self.checkStopFlag():
                            self.shelf.setAll(0, 0, 0)
                            self.shelf.update()
                            break

                        time.sleep(.005)

                    for i in range(100):
                        newR = int((hazeR * ((100.0 - i) / 100.0)) + (self.r * (i / 100.0)))
                        newG = int((hazeG * ((100.0 - i) / 100.0)) + (self.g * (i / 100.0)))
                        newB = int((hazeB * ((100.0 - i) / 100.0)) + (self.b * (i / 100.0)))

                        self.shelf.setAll(newR, newG, newB)
                        self.shelf.update()

                        if self.checkStopFlag():
                            self.shelf.setAll(0, 0, 0)
                            self.shelf.update()
                            break

                        time.sleep(.005)
            #clear
            elif self.weatherId == 8:
                break


            if self.checkStopFlag():
                self.shelf.setAll(0, 0, 0)
                self.shelf.update()
                break


            self.shelf.update()
            time.sleep(0.5)
            tick += 1




