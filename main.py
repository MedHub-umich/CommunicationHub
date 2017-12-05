from connect import *
from threads import *
import time

connectedDevs = connect()
# connectedDevs.startRead(0)

time.sleep(2)

while(1):
	writeTo(connectedDevs[0],  "00020101")
	time.sleep(2)
	writeTo(connectedDevs[1], "00020101")
	time.sleep(2)
	writeTo(connectedDevs[0],  "00020001")
	time.sleep(2)
	writeTo(connectedDevs[1], "00020001")
	time.sleep(2)
while(1):
	pass
