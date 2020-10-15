import os
from time import sleep
import random
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
while True:
    if (GPIO.input(6) == True):
       print ("Touch")
       GPIO.output(26, GPIO.LOW)
       sleep(10)
    else:
        GPIO.output(26, GPIO.HIGH)
        print ("Release")
