#!/usr/bin/env python

import time
import board
import neopixel
import shelf as s
import events
import keyboard


def dispay(shelf, pixels):
    
    for square in shelf.squares:
        for led in square.led_list:
            pixels[led] = (square.getRed(), square.getGreen(), square.getBlue())

    pixels.show()


def userInput(shelf, event):
    try:
        if keyboard.is_pressed('0'):
            event = events.Off(shelf)
        if keyboard.is_pressed('1'):
            event = events.StaticOrange(shelf)
        if keyboard.is_pressed('2'):
            event = events.Fade(shelf)
        if keyboard.is_pressed('3'):
            event = events.StaticWhite(shelf)
    except:
        print()
    return event


numsqares = 13
shelf = s.Shelf(numsqares)
tick = 1/60 # 60 fps
pixels = neopixel.NeoPixel(board.D18, numsqares * 4, auto_write=False)
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
    
