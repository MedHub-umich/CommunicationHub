
class Device:
	def __init__(self, MACaddress, devHandle):
		self.MACaddress = MACaddress;
		self.devHandle = devHandle;

 #TODO :
 #	- implement device class?
 # 	- pull GPIO stuff into an interface?

 #Next steps:
 # 	- test mainThreading.py
 #  - make writes "interrupt based", AKA from GPIO pins
