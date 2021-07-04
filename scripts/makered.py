#!/usr/bin/env python

import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 100)
pixels.fill((200, 30, 0))