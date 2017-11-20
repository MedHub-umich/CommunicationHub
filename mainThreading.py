import threading
import time
from connect import Devices, readFrom, writeTo

def readFromThread(devHandle):
	readFrom(devHandle)

def writeToThread(devHandle):
	time.sleep(5)
	writeTo(devHandle, alert)

def main():
	global alert = 00020000

	threads = []

	BLEdevs = Devices()

	connectedDevs = devices.connectDevices()
	while(len(connectedDevs) == 0):
		connectedDevs = devices.connectDevices()

	for i in connectDevs:  # may have bug off by one
		threads.append(threading.Thread(name = "dev"+i, target = readFromThread, args = connectedDevs[i])) #possible bug
		threads[i].setDaemon(True)
		threads[i].start()

	#possibly have to manually reset i?

	for i in connectedDevs:
		threads.append(threading.Thread(name = "dev"+i, target = writeToThread, args = connectedDevs[i]))
		threads[i].setDaemon(True)
		threads[i].start()

	alertValues = [00020000, 00020100, 00020101, 00020001]

	for j in alertValues:
		alert = alertValues[j]
		time.sleep(5)






