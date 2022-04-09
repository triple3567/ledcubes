import sqlite3
import time

class DBHandler():

    def __init__(self):
        self.con = sqlite3.connect("../data/ledcubes.db", check_same_thread=False)
        return
    
    def configTables(self):
        self.con.execute('''CREATE TABLE IF NOT EXISTS SCANNER_LOG
                            (scannerID INTEGER NOT NULL, tagID INTEGER, data TEXT, timestamp INTEGER, id INTEGER PRIMARY KEY)
        ''')
        self.con.commit()

    def insertScan(self, scannerID, tagID = 'NULL', data = 'NULL'):

        if tagID == None:
            tagID = 'NULL'

        if data == None:
            data = 'NULL'

        scannerID = str(scannerID)
        timestamp = str((int(time.time())))
        tagID = str(tagID)
        data = str(data)
        query = f'''INSERT INTO SCANNER_LOG 
                    (scannerID, tagID, data, timestamp) 
                    VALUES ({scannerID}, {tagID}, '{data}', {timestamp});'''

        self.con.execute(query)
        self.con.commit()

        #clean up old scans here (delete old scans when table len > 1000ish)

    def getLatestScan(self, scannerID):
        scannerID = str(scannerID)

        query = f'''SELECT scannerID, tagID, data, timestamp, MAX(id) FROM SCANNER_LOG  
                    WHERE scannerID == {scannerID} 
                    GROUP BY scannerID;'''

        res = self.con.execute(query)
        '''
        for row in res:
            print('scannerID = ', row[0])
            print('tagID = ', row[1])
            print('data = ', row[2])
            print('timestamp = ', row[3])
            print('id = ', row[4])
        '''

        #returns tagID, data, timestamp, id
        for row in res:
            return row[1], row[2], row[3], row[4]

        return None, None, None, None

    #Gets the scan with the lowest id greater than the id provided
    def getScanAfterID(self, scannerID, id):
        scannerID = str(scannerID)
        id = str(id)

        query = f'''SELECT scannerID, tagID, data, timestamp, MIN(id) FROM SCANNER_LOG
                    WHERE scannerID == {scannerID} AND id > {id} 
                    GROUP BY scannerID;'''
        
        res = self.con.execute(query)

        #returns tagID, data, timestamp, id
        for row in res:
            return row[1], row[2], row[3], row[4]

    def getAll(self, scannerID):
        scannerID = str(scannerID)

        query = f'''SELECT scannerID, tagID, data, timestamp, id FROM SCANNER_LOG
                    WHERE scannerID == {scannerID}
                    ORDER BY id desc;'''

        res = self.con.execute(query)

        return res        

    def clearScannerLog(self):
        query = '''DELETE FROM SCANNER_LOG'''
        self.con.execute(query)
        self.con.commit()

if __name__ == '__main__':
    
    dbHandler = DBHandler()

    print("Running Database Debuging Program...")

    while True:
        print()
        choice = int(input("1. Insert Scan\n2. Select All Scans\n3. Select latest from Scanner\n4. Clear ScannerLog\n-1. Quit... "))


        if choice == 1:
            print()
            scannerID = int(input("scannerID? "))
            tagID = int(input("tagID? "))
            data = str(input("data? "))

            dbHandler.insertScan(scannerID, tagID, data)
        elif choice == 2:

            for i in range(9):
                res = dbHandler.getAll(i)

                for row in res:
                    print()
                    print('scannerID = ', row[0])
                    print('tagID = ', row[1])
                    print('data = ', row[2])
                    print('timestamp = ', row[3])
                    print('id = ', row[4])

        elif choice == 3:
            print()
            scannerID = int(input("scannerID? "))
            tagID, data, timestamp, id = dbHandler.getLatestScan(scannerID)

            print()
            print('scannerID = ', scannerID)
            print('tagID = ', tagID)
            print('data = ', data)
            print('timestamp = ', timestamp)
            print('id = ', id)

        elif choice == 4:
            dbHandler.clearDB()
            print()
            print("ScannerLog Table Cleared")
        elif choice == -1:
            break
            