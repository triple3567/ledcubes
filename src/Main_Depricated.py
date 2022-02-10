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

        elif keyboard.is_pressed('r'):
            event = events.BreathingOrange(shelf)

        elif keyboard.is_pressed('t'):
            event = events.BreathingWhite(shelf)


        #GAME

    except:
        print("ERROR SETTING EVENT")
    return event

print("BREAK 1")

numsqares = 9
ledpersquare = 9
shelf = s.Shelf(numsqares)
tick = 1/20 # 20 fps

pixels = neopixel.NeoPixel(board.D18, numsqares * ledpersquare, auto_write=False)

print("BREAK 2")

event = events.Fade2(shelf)

print("BREAK 3")


t0 = time.time()
count = 0

while True:

    print("BREAK 4")

    t1 = time.time()
    while t1 - t0 < tick:
        t1 = time.time()

    print("BREAK 5")

    count += 1
    t0 = t1

    shelf = event.next(count)

    print("BREAK 6")

    dispay(shelf,pixels)

    print("BREAK 7")

    userInput(shelf, event)

    print("BREAK 8")

    if count > 9999:
        count = 0
    
    print(f"frame: %", count)
