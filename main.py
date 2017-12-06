from connect import *
import time
import mainWrite

connectedDevs = connect()
mainWrite.writer(connectedDevs)
while (1):
	pass
