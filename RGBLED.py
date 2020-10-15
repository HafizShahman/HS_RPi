import RPi.GPIO as GPIO             #import the raspberry pi GPIO library, to be able to use them.
from time import sleep              #import the sleep library, which responsible to do the timing stuff.


redLED = 16
greenLED = 20
blueLED = 21

redLED2 = 13
greenLED2 = 19
blueLED2 = 26

GPIO.setwarnings(False)   #disable warnings
GPIO.setmode(GPIO.BCM)         #set pin numbering system to the (Broadcom chip channel numbering).

GPIO.setup(redLED,GPIO.OUT)     #set the red LED pin(GPIO18) to an output pin.
GPIO.setup(blueLED,GPIO.OUT)    #set the blue LED pin(GPIO12) to an output pin.
GPIO.setup(greenLED,GPIO.OUT)   #set the green LED pin(GPIO19) to an output pin.

GPIO.setup(redLED2,GPIO.OUT)     #set the red LED pin(GPIO18) to an output pin.
GPIO.setup(blueLED2,GPIO.OUT)    #set the blue LED pin(GPIO12) to an output pin.
GPIO.setup(greenLED2,GPIO.OUT)   #set the green LED pin(GPIO19) to an output pin.


red_pwm = GPIO.PWM(redLED,1000)               #create PWM instance with 1000Hz frequency.
blue_pwm = GPIO.PWM(blueLED,1000)             #create PWM instance with 1000Hz frequency.
green_pwm = GPIO.PWM(greenLED,1000)           #create PWM instance with 1000Hz frequency.

red_pwm2 = GPIO.PWM(redLED2,1000)               #create PWM instance with 1000Hz frequency.
blue_pwm2 = GPIO.PWM(blueLED2,1000)             #create PWM instance with 1000Hz frequency.
green_pwm2 = GPIO.PWM(greenLED2,1000)           #create PWM instance with 1000Hz frequency.

red_pwm.start(0)                  #start red LED PWM pin with 0% initial Duty Cycle (OFF).
blue_pwm.start(0)                             #start blue LED PWM pin with 0% initial Duty Cycle (OFF).
green_pwm.start(0)                            #start green LED PWM pin with 0% initial Duty Cycle (OFF).

red_pwm2.start(0)                  #start red LED PWM pin with 0% initial Duty Cycle (OFF).
blue_pwm2.start(0)                             #start blue LED PWM pin with 0% initial Duty Cycle (OFF).
green_pwm2.start(0)                            #start green LED PWM pin with 0% initial Duty Cycle (OFF).

print("AH Shit! Here we go again! Press CTRL+C to exit")    #Take Care, Meme LORD.

try:
    while True:                                         #the start of the actual program.
        for duty in range(0,101,1):                     #imolement a "for loop" responsible for increasing the red LED light brightness.
            red_pwm.ChangeDutyCycle(duty)               #provide duty cycle in the range 0-100.
            red_pwm2.ChangeDutyCycle(duty)               #provide duty cycle in the range 0-100.
            sleep(0.01)                                 #wait 0.01 sec. between each iteration.
        sleep(0.5)                                      #wait 0.5 sec. after the "for loop" is done.

        for duty in range(100,-1,-1):                   #implement a "for loop" responsible for decreasing the red LED light brightness.
            red_pwm.ChangeDutyCycle(duty)               #provide duty cycle in the range 100-0.
            red_pwm2.ChangeDutyCycle(duty)               #provide duty cycle in the range 0-100.
            sleep(0.01)                                 #wait 0.01 sec. between each iteration.
        sleep(0.5)                                      #wait 0.5 sec. after the "for loop" is done.
  
        for duty in range (0, 101, 1):                  #repeat the previous logic but this time with the blue LED.
            blue_pwm.ChangeDutyCycle(duty)
            blue_pwm2.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

        for duty in range (100, -1, -1):                #repeat the previous logic but this time with the blue LED.
            blue_pwm.ChangeDutyCycle(duty)
            blue_pwm2.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

        for duty in range(0,101,1):                     #repeat the previous logic but this time with the green LED.
            green_pwm.ChangeDutyCycle(duty)
            green_pwm2.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

        for duty in range(100,-1,-1):
#repeat the previous logic but this time with the green LED.
            green_pwm.ChangeDutyCycle(duty)
            green_pwm2.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

except KeyboardInterrupt:   # If CTRL+C is pressed, exit cleanly:
    red_pwm.stop()        # stop red PWM
    blue_pwm.stop()             # stop blue PWM
    green_pwm.stop()            # stop green  PWM
    red_pwm2.stop()        # stop red PWM
    blue_pwm2.stop()             # stop blue PWM
    green_pwm2.stop()            # stop green  PWM
    GPIO.cleanup()              # cleanup all GPIO