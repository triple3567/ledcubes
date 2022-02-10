#!/usr/bin/env python

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 92)
pixels.fill((255, 0, 0))
# pixels[21] = ((200, 30, 0))
