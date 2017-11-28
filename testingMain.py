import threading
import time
from connect import Devices, readFrom, writeTo

def readFromThread(devHandle):
	readFrom(devHandle)

def writeToThread(devHandle, value):
	time.sleep(2)
	writeTo(devHandle, value)

threads = []

BLEdevs = DeviceContainer()

connectedDevs = BLEdevs.connectDevices()
while(len(connectedDevs) == 0):
	connectedDevs = BLEdevs.connectDevices()

threads.append(threading.Thread(target=readFromThread, args=(connectedDevs[0].devHandle,)))
threads[0].setDaemon(True)
threads[0].start() 

#threads.append(threading.Thread(target=writeToThread, args=(connectedDevs[0], "00020101")))
#threads[0].setDaemon(True)
#threads[0].start()

time.sleep(5)

threads.append(threading.Thread(target=writeToThread, args=(connectedDevs[0].devHandle, "00020101")))
threads[1].setDaemon(True)
threads[1].start()


time.sleep(5)