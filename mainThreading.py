import threading
import time
from connect import Devices, readFrom, writeTo

def readFromThread(devHandle):
	readFrom(devHandle)

def writeToThread(devHandle):
	time.sleep(5)
	writeTo(devHandle, alert)

def main():
	global alert

	threads = []

	BLEdevs = Devices()

	connectedDevs = BLEdevs.connectDevices()
	while(len(connectedDevs) == 0):
		connectedDevs = BLEdevs.connectDevices()
	
	i = 0
	for i, device in connectedDevs:  # may have bug off by one
		threads.append(threading.Thread(target = readFromThread, args = device)) #possible bug
		threads[i].setDaemon(True)
		threads[i].start()

	#possibly have to manually reset i?
	
	for i,device in connectedDevs:
		threads.append(threading.Thread(target = writeToThread, args = device))
		threads[i].setDaemon(True)
		threads[i].start()

	alertValues = [00020000, 00020100, 00020101, 00020001]

	for j in alertValues:
		alert = alertValues[j]
		time.sleep(5)

main()




