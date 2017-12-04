import threading
import time
from connect import *

def readFromThread(devHandle):
	readFrom(devHandle)

def writeToThread(devHandle, value):
	time.sleep(2)
	writeTo(devHandle, value)

threads = []   #TODO: currently not deleting threads after they have completed
numThreads = 0 

def connect():
	BLEdevs = DeviceContainer()

	connectedDevs = BLEdevs.connectDevices()
	while(len(connectedDevs) == 0):
		connectedDevs = BLEdevs.connectDevices()

	return connectedDevs


def BLEread(device):
	global threads
	global numThreads
	threads.append(threading.Thread(target=readFromThread, args=(device,)))
	threads[numThreads].setDaemon(True)
	# pull this out so it gets initialized then start read is where it will start working???s	
	threads[numThreads].start()
	numThreads = numThreads + 1 

def BLEwrite(device, value):
	global threads
	global numThreads
	threads.append(threading.Thread(target=writeToThread, args=(device.devHandle, value)))
	threads[numThreads].setDaemon(True)
	threads[numThreads].start()
	numThreads = numThreads + 1

def reconnect(device):
	global threads
	global numThreads

#.cancel() to stop a thread 
#.terminate() to close spawn


