import RPi.GPIO as GPIO
Import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIOIN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        subprocess.call("/home/pi/Documents/MedHub/CommunicationHub", shell=True)