from SimpleMFRC522 import SimpleMFRC522 
import time
import threading
import copy
from DBHandler import DBHandler
import logging

'''
DATA FORMAT

EVENT:FADE
ITEM:ITEMDESCRIPTION:ITEMID
COLOR:COLORNAME


'''


class RfidHandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        logging.basicConfig(filename='../logs/LEDCubes.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)

        self.readers = []
        self.readers.append(SimpleMFRC522(device=0))
        self.readers.append(SimpleMFRC522(device=1))
        self.readers.append(SimpleMFRC522(device=2))
        self.readers.append(SimpleMFRC522(device=3))
        self.readers.append(SimpleMFRC522(device=4))
        self.readers.append(SimpleMFRC522(device=5))
        self.readers.append(SimpleMFRC522(device=6))
        self.readers.append(SimpleMFRC522(device=7))
        self.readers.append(SimpleMFRC522(device=8))

        self.dbHandler = DBHandler()

        self.activeScanners = {
            0: True,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False
        }

    def enableAll(self):
        for key in self.activeScanners:
            self.activeScanners[key] = True

    def disableAll(self):
        for key in self.activeScanners:
            self.activeScanners[key] = False
    
    def enable(self, index):
        self.activeScanners[index] = True

    def disable(self, index):
        self.activeScanners[index] = False

    def scan(self, index):
        try:
            tagID, data = self.readers[index].read_no_block()

            return tagID, data

        except:
            return


    def run(self):
        
        while True:

            for key in self.activeScanners:
                
                if self.activeScanners[key]:

                    tagID, data = self.scan(key)
                    self.dbHandler.insertScan(key, tagID, data)

                    #logging.info("scanner = " + str(key) + " - data = " + str(data) + " - tagID = " + str(tagID))

if __name__ == '__main__':
    rfidHandler = RfidHandler()
    rfidHandler.start()
    rfidHandler.join()