from threading import *
import requests


class writeWorker(Thread):
	def __init__(self, device, data):
		Thread.__init__(self)
		self.device = device
		self.data = data
		self.daemon = True
		self.start()

	def run(self):
		command = "char-write-req 0x0019 " + self.data
		if self.device.isConnected == False:
			# print("waiting to send..")
			# time.sleep(2)
			print("This device is not connected")
			return

		self.device.devHandle.sendline(command)
		print("Write Successful", self.device)