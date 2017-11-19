import threading
import time

class Device:
	def __init__(self, MACaddress, devHandle):
		self.MACaddress = MACaddress
		self.devHandle = devHandle

def threadTest(device):
	print device.MACaddress,
	print "\n"

def threadTest2(device):
	print device.devHandle,
	print "\n"

def infiniteThread():
	while True:
		print "still running!"

device1 = Device("22:22:22:22", "this is a handle")
device2 = Device("11:11:11:11", "this is another handle")

thread1 = threading.Thread(name = "test1", target=threadTest, args=(device1,))
thread1.start()
print "first thread started"



thread3 = threading.Thread(name = "test3", target=infiniteThread)
thread3.setDaemon(True)
thread3.start()

thread2 = threading.Thread(name = "test2", target=threadTest2, args=(device2,))
thread2.start()
print "second thread started"

time.sleep(1)
