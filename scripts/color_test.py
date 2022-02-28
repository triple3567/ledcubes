import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 92)

r = int(input("Enter red value: "))
g = int(input("Enter green value: "))
b = int(input("Enter blue value: "))

pixels.fill((r, g, b))
# pixels[21] = ((200, 30, 0))