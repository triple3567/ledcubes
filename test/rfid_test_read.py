import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 
import time

reader0 = SimpleMFRC522(device=0, spd=700000)

reader1 = SimpleMFRC522(device=1, spd=700000)
time.sleep(1)

try:
        id, text = reader0.read()
        print(id)
        print(text)

        id, text = reader1.read()
        print(id)
        print(text)

finally:
        GPIO.cleanup()