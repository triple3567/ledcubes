from EventSequence import *
from RfidHandler import RfidHandler
import color_constants
import pprint
from DBHandler import DBHandler
import logging

event = Off()
event.start()

rfidHandler = RfidHandler()
rfidHandler.start()
rfidHandler.enableAll()

dbHandler = DBHandler()
dbHandler.configTables()
tagID, data, timestamp, id = dbHandler.getLatestScan(0)
currID = id

logging.basicConfig(filename='../logs/LEDCubes.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)

choice = 'fade'
newChoiceFlag = True

while True:

    if newChoiceFlag:
        print(choice)
        choice = choice.strip()
        if choice == 'off':
            event.stop()
            event.join()
            event = Off()
            event.start()
        elif choice == 'color':
            continue
        elif choice == 'fade':
            event.stop()
            event.join()
            event = Fade()
            event.start()
        elif choice == 'circle':
            event.stop()
            event.join()
            event = Circle()
            event.start()
        elif choice == 'bounce':
            event.stop()
            event.join()
            event = Bounce()
            event.start()
        elif choice == 'weather':
            event.stop()
            event.join()
            event = Weather()
            event.start()
        elif choice == 'color_combination':
            event.stop()
            event.join()
            event = ColorCombination()
            event.start()

        newChoiceFlag = False

    tagID, data, timestamp, id = dbHandler.getLatestScan(0)
    #logging.debug("data = " + str(data) + " - databaseID = " + str(id))

    if data != None:
        parsed = data.split(':')
        if parsed[0] == 'event':

            if choice != parsed[1].strip():
                choice = parsed[1]
                
                newChoiceFlag = True


    
    


