import qwiic
import qwiic_rfid
import time
import sys

"""
test = qwiic.QwiicTCA9548A()

# Enable Channels 0 and 1
test.enable_channels([0])
test.list_channels()
"""

print("\nSparkFun Qwiic RFID Reader Example 1")
#my_RFID = qwiic_rfid.QwiicRFID(address=0x70)
my_RFID = qwiic_rfid.QwiicRFID()

if my_RFID.begin() == False:
    print("\nThe Qwiic RFID Reader isn't connected to the system. Please check your connection", file=sys.stderr)
    

print("\nReady to scan some tags!")

my_RFID.clear_tags()

while True:
    val = input("\nEnter 1 to get tag ID and scan time: ")

    if int(val) == 1:
        print("\nGetting your tag ID...")
        tag = my_RFID.get_tag()
        print("\nTag ID: " + tag)

        scan_time = my_RFID.get_prec_req_time()
        # If this time is too precise, try:
        # scan_time = my_RFID.get_req_time()
        print("\nScan Time: " + str(scan_time))
    
    time.sleep(0.02)