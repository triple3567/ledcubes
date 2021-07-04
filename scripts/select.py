import board
import neopixel
import sys

pixels = neopixel.NeoPixel(board.D18, 30)

print('Number of arguments:', len(sys.argv), 'arguments.')

pixels[int(sys.argv[1])] = (255,255,255)