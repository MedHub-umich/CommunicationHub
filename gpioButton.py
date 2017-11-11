
# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 17 # Broadcom pin 17 (P1 pin 11)
status = 0

def buttonISR(channel):
    global status
    print ("in ISR")
    if (status>0):
        GPIO.output(ledPin, GPIO.HIGH)
        status = 0
    else:
        GPIO.output(ledPin, GPIO.LOW)
        status = 1

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
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
