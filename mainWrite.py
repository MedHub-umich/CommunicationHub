from threading import *
import requests
import individualWrite
import config
import time

Users = [1, 2]

class writer(Thread):
	def __init__(self, connectedDevs):
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
				r = requests.get('http://medhub-server.herokuapp.com/api/v1.0/alert/' + str(user))
				r = r.json()
				if len(r['alerts']) > 0 and not userDevice is None:
					for alert in r['alerts']:
						print ("Sending alert "),
						print (alert['data'])
						individualWrite.writeWorker(userDevice, alert['data'])
				else:
					print("No alert found for user: "),
					print(user)
			time.sleep(2)




