import os
from time import sleep
import random
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
while True:
    if (GPIO.input(13) == True):
       print ("Hello")
       GPIO.output(20, GPIO.LOW)
       GPIO.output(15, GPIO.HIGH)
       GPIO.output(14, GPIO.LOW)
       sleep(10)
    else:
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(14, GPIO.LOW)
        #print ("Dah settle")
