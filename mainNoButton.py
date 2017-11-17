from connect import Devices, readFrom, writeTo
import time

devices = Devices()

connectedDevs = devices.connectDevices()
while(len(connectedDevs) == 0):
	connectedDevs = devices.connectDevices()

readFrom(connectedDevs[0])

writeTo(connectedDevs[0], "00020101")
time.sleep(5)
writeTo(connectedDevs[0], "00020001")
time.sleep(5)
writeTo(connectedDevs[0], "00020000")
time.sleep(5)
writeTo(connectedDevs[0], "00020100")
	
