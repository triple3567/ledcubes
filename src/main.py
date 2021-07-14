#!/usr/bin/env python

import time
import board
import neopixel
import shelf as s
import events
import keyboard


def dispay(shelf, pixels):
    
    for col in shelf.squares:
        for square in col:
            for led in square.led_list:
                pixels[led] = (square.getRed(), square.getGreen(), square.getBlue())

    pixels.show()


def userInput(shelf, event):
    try:
        
        #STATIC
        if keyboard.is_pressed('0'):
            
            event = events.Off(shelf)

        elif keyboard.is_pressed('1'):

            event = events.StaticOrange(shelf)

        elif keyboard.is_pressed('2'):
            event = events.StaticWhite(shelf)


        #TRANSITION
        elif keyboard.is_pressed('q'):

            event = events.Fade(shelf)

        elif keyboard.is_pressed('w'):
            event = events.Fade2(shelf)

        elif keyboard.is_pressed('e'):
            event = events.Slide(shelf)

        #GAME

    except:
        print("ERROR SETTING EVENT")
    return event


numsqares = 9
ledpersquare = 9
shelf = s.Shelf(numsqares)
tick = 1/60 # 60 fps
pixels = neopixel.NeoPixel(board.D18, numsqares * ledpersquare, auto_write=False)
event = events.Fade(shelf)

t0 = time.time()
count = 0

while True:

    t1 = time.time()
    while t1 - t0 < tick:
        t1 = time.time()

    count += 1
    t0 = t1

    shelf = event.next(count)
    dispay(shelf,pixels)

    event = userInput(shelf, event)

    if count > 9999:
        count = 0
    
