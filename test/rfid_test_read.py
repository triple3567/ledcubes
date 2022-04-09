import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 
import time


reader0 = SimpleMFRC522(device=0)
reader1 = SimpleMFRC522(device=1)
reader2 = SimpleMFRC522(device=2)
reader3 = SimpleMFRC522(device=3)
reader4 = SimpleMFRC522(device=4)
reader5 = SimpleMFRC522(device=5)
reader6 = SimpleMFRC522(device=6)
reader7 = SimpleMFRC522(device=7)
reader8 = SimpleMFRC522(device=8)
time.sleep(1)

try:
        
        id, text = reader0.read()
        print("0 id = " + str(id))
        print("data = " + str(text))
        
        id, text = reader1.read()
        print("1 id = " + str(id))
        print("data = " + str(text))

        id, text = reader2.read()
        print("2 id = " + str(id))
        print("data = " + str(text))
        

        id, text = reader3.read()
        print("3 id = " + str(id))
        print("data = " + str(text))
        
        id, text = reader4.read()
        print("4 id = " + str(id))
        print("data = " + str(text))

        id, text = reader5.read()
        print("5 id = " + str(id))
        print("data = " + str(text))
        
        id, text = reader6.read()
        print("6 id = " + str(id))
        print("data = " + str(text))

        id, text = reader7.read()
        print("7 id = " + str(id))
        print("data = " + str(text))

        id, text = reader8.read()
        print("8 id = " + str(id))
        print("data = " + str(text))
        

finally:
        GPIO.cleanup()