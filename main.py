from threads import *
import time

connectedDevs = connect()
BLEread(connectedDevs[0])

time.sleep(2)

BLEwrite(connectedDevs[0],  "00020101")

time.sleep(2)

