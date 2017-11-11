from connect import Devices
from connect import readFrom

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)
connect = 0
timeOut = 0
ledState = False
def buttonISR(channel):
	global connect
	global timeOut
	global DEVICES

	Devices()
	connect = 1 
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(5)
	timeOut = 1
	readFrom(0)


# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

    
GPIO.add_event_detect(17, GPIO.FALLING, callback = buttonISR, bouncetime=300)
print("Here we go! Press CTRL+C to exit")
try:
    while 1:
	    if (connect == 0 and timeOut == 0):
		ledState = not ledState
		GPIO.output(ledPin, ledState)
	    elif (connect == 1 and timeOut == 0):
		GPIO.output(ledPin, GPIO.HIGH)
	    elif (connect == 1 and timeOut == 1):
		GPIO.output(ledPin, GPIO.LOW)

	    

            time.sleep(0.3)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO