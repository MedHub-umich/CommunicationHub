import threading
import time
from connect import DeviceContainer, readFrom, writeTo

def readFromThread(devHandle):
	readFrom(devHandle)

def writeToThread(devHandle, value):
	time.sleep(2)
	writeTo(devHandle, value)

threads = []
numThreads = 0 

def connect():
	BLEdevs = DeviceContainer()

	connectedDevs = BLEdevs.connectDevices()
	while(len(connectedDevs) == 0):
		connectedDevs = BLEdevs.connectDevices()

	return connectedDevs


def read(device):
	threads.append(threading.Thread(target=readFromThread, args=(device.devHandle,)))
	numThreads = numThreads + 1
	threads[numThreads].setDaemon(True)
	threads[numThreads].start() 

def write(device, value):
	threads.append(threading.Thread(target=writeToThread, args=(device.devHandle, "00020101")))
	numThreads = numThreads + 1
	threads[numThreads].setDaemon(True)
	threads[numThreads].start()



# threads.append(threading.Thread(target=writeToThread, args=(connectedDevs[0].devHandle, "00020101")))
# threads[2].setDaemon(True)
# threads[2].start()


time.sleep(2)