import RPi.GPIO as GPIO
import time
import pexpect
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        pexpect.spawn("sudo python /home/pi/Documents/MedHub/CommunicationHub/main.py")