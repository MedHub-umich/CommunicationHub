from connect import *
from threads import *
import time

connectedDevs = connect()
startRead(connectedDevs[0])

time.sleep(2)

BLEwrite(connectedDevs[0],  "00020101")

while(1):
	pass
