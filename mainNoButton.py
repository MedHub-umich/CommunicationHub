from connect import Devices, readFrom



devices = Devices()

connectedDevs = devices.connectDevices()
while(len(connectedDevs) == 0):
	connectedDevs = devices.connectDevices()

readFrom(connectedDevs[0])

