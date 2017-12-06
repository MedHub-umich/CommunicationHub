from threading import *
import requests
import individualWrite
import config

Users = [1, 2]

class writer(Thread, connectedDevs):
	def __init__(self):
		Thread.__init__(self)
		self.connectedDevs = connectedDevs
		self.start()

	def run(self):
		while (1):
			for user in Users:
				userDevice = None
				macAddr = config.userToMac[user]
				for dev in self.connectedDevs:
					if dev.MACaddress == macAddr:
						userDevice = dev
				r = requests.get('medhub-server.herokuapp.com/api/v1.0/alert/' + str(user));
				if len(r.alerts) > 0 and userDevice not is None:
					for alert in r.alerts:
						individualWrite.writeWorker(userDevice, alert.data)



