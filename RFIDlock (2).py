import sys
import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
import time
CardRead = SimpleMFRC522()
 
load1 = 13
 
gpio.setmode(gpio.BOARD)
#gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(load1,gpio.OUT)

#idlist = '31389199508', '49048004155'
 
print ('Card Scanning')
print ('for Cancel Press ctrl+c')
 
try:
    while True:
        
        id, text = CardRead.read()
        print(id)
        print(text) 
        if id == 31389199508:
            if gpio.input(load1):
                gpio.output(load1,gpio.LOW)
                print('Un-Lock')
                time.sleep(5)
                gpio.output(load1,gpio.HIGH)
                print('Lock')
            else:
                gpio.output(load1,gpio.HIGH)
                print('Lock')
                
 
except KeyboardInterrupt:
    gpio.cleanup()