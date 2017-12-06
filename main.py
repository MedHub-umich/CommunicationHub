from connect import *
import time

# For button press
import RPi.GPIO as GPIO

# Pin Definitions:
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)
connect = 0
timeOut = 0
ledState = False


connectedDevs = connect()

time.sleep(2)

while(1):
	writeTo(connectedDevs[0],  "00020101")
	time.sleep(2)
	writeTo(connectedDevs[1], "00020101")
	time.sleep(2)
	writeTo(connectedDevs[0],  "00020001")
	time.sleep(2)
	writeTo(connectedDevs[1], "00020001")
	time.sleep(2)
while(1):
	pass
