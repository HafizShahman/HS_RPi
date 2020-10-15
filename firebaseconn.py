import RPi.GPIO as GPIO                                                                         #import the RPi.GPIO module to allow us use the board GPIO pins.
import pyrebase                                                                                 #import the pyrebase module which allows us to communicate with the firebase servers.
from time import sleep                                                                          #import the time modulde to allow us do the delay stuff.
config = {                                                              #define a dictionary named config with several key-value pairs that configure the connection to the database.
  "apiKey": "AIzaSyCNHPB9MH2RR4kKwHlkoBEop1skxLR_TDo",
  "authDomain": "smart-door-3ab68.firebaseapp.com",
  "databaseURL": "https://smart-door-3ab68.firebaseio.com/",
  "storageBucket": "smart-door-3ab68.appspot.com"
}
firebase = pyrebase.initialize_app(config)                              #initialize the communication with the "firebase" servers using the previous config data.
redLED = 16                                                                                    #the "redLED" variable refers to the GPIO pin 12 which the red LED is connected on.
blueLED = 21                                                                                   #the "blueLED" variable refers to the GPIO pin 19 which the blue LED is connected on.
greenLED = 20                                                                                  #the "greenLED" variable refers to the GPIO pin 18 which the green LED is connected on.
GPIO.setmode(GPIO.BCM)                                                                         #Set the GPIO Scheme numbering system to the BCM mode.
GPIO.setwarnings(False)                                                                        #disable warnings
GPIO.setup(redLED,GPIO.OUT)                                                                    #set the "redLED" variable pin (12) as an output pin.
GPIO.setup(blueLED,GPIO.OUT)                                                                   #set the "blueLED" variable pin (19) as an output pin.
GPIO.setup(greenLED,GPIO.OUT)                                                                  #set the "greenLED" variable pin (18) as an output pin.
red_pwm = GPIO.PWM(redLED,1000)                                                                #create PWM instance named "red_pwm" with frequency 1000.
blue_pwm = GPIO.PWM(blueLED,1000)                                                              #create PWM instance named "blue_pwm" with frequency 1000.
green_pwm = GPIO.PWM(greenLED,1000)                                                            #create PWM instance named "green_pwm" with frequency 1000.
red_pwm.start(0)                                                                               #start the program with 0% duty cycle (red LED will be OFF).
blue_pwm.start(0)                                                                              #start the program with 0% duty cycle (blue LED will be OFF).
green_pwm.start(0)                                                                             #start the program with 0% duty cycle (green LED will be OFF).
print("AH Shit! Here we go again! Press CTRL+C to exit")                                       #print "AH Shit! Here we go again! Press CTRL+C to exit" at the beginning of the program.
# function name: mode6
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the lighting pattern as you want.
def mode6 (redIntensity, greenIntensity, blueIntensity):
    for duty in range (0, redIntensity, 1):
        red_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.3)
    for duty in range (redIntensity - 1, -1, -1):
        red_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.3)
    for duty in range (0, blueIntensity, 1):
        blue_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.3)
    for duty in range (blueIntensity - 1, -1, -1):
        blue_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.3)
    for duty in range (0, greenIntensity, 1):
        green_pwm.ChangeDutyCycle(duty)              #provide duty cycle in the range 0-100.
        sleep(0.01)
    sleep(0.3)
    for duty in range (greenIntensity - 1, -1 ,-1):
       green_pwm.ChangeDutyCycle(duty)               #provide duty cycle in the range 0-100
       sleep(0.01)
    sleep(0.3)
# function name: mode5
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the lighting pattern as you want.
def mode5(redIntensity, greenIntensity, blueIntensity):
    for duty in range (0, redIntensity, 1):
        red_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    sleep(0.3)
    for duty in range (redIntensity - 1, -1, -1):
        red_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    sleep(0.3)
    for duty in range (0, blueIntensity, 1):
        blue_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    sleep(0.3)
    for duty in range (blueIntensity - 1 , -1, -1):
        blue_pwm.ChangeDutyCycle(duty)
        sleep(0.001)
    sleep(0.3)
    for duty in range (0, greenIntensity, 1):
        green_pwm.ChangeDutyCycle(duty)              #provide duty cycle in the range 0-100.
        sleep(0.001)
    sleep(0.3)
    for duty in range (greenIntensity - 1 , -1, -1):
       green_pwm.ChangeDutyCycle(duty)               #provide duty cycle in the range 0-100
       sleep(0.001)
    sleep(0.3)
# function name: mode4
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the lighting pattern as you want.
def mode4(redIntensity, greenIntensity, blueIntensity):
    for duty in range (0, redIntensity, 1):
        red_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)
    green_pwm.ChangeDutyCycle(0)
    sleep(0.2)
    green_pwm.ChangeDutyCycle(greenIntensity - 1)
    for duty in range (0, blueIntensity, 1):
        blue_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)
    blue_pwm.ChangeDutyCycle(0)
    sleep(0.2)
    blue_pwm.ChangeDutyCycle(blueIntensity - 1)
    for duty in range (0,greenIntensity,1):
        green_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)
    red_pwm.ChangeDutyCycle(0)
    sleep(0.2)
    red_pwm.ChangeDutyCycle(redIntensity - 1)
    red_pwm.ChangeDutyCycle(0)
    green_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(0)
# function name: mode3
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the lighting pattern as you want.
def mode3(redIntensity, greenIntensity, blueIntensity):
    red_pwm.ChangeDutyCycle(0)
    green_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(0)
    red_pwm.ChangeDutyCycle(redIntensity - 1)
    blue_pwm.ChangeDutyCycle(blueIntensity - 1)
    green_pwm.ChangeDutyCycle(greenIntensity - 1)
# function name: mode2
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the
#lighting pattern as you want.
def mode2(redIntensity, greenIntensity, blueIntensity):
    red_pwm.ChangeDutyCycle(0)
    green_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(blueIntensity - 1)
    sleep(0.1)
    blue_pwm.ChangeDutyCycle(0)
    sleep(0.1)
    green_pwm.ChangeDutyCycle(greenIntensity - 1)
    sleep(0.1)
    green_pwm.ChangeDutyCycle(0)
    sleep(0.1)
    red_pwm.ChangeDutyCycle(redIntensity - 1)
    sleep(0.1)
    red_pwm.ChangeDutyCycle(0)
    sleep(0.1)
# function name: mode1
# arguments:
#   redIntensity: the brightness intensity of the red LED.
#   greenIntensity: the brightness intensity of the green LED.
#   blueIntensity: the brightness intensity of the blue LED.
# return: this funtion return nothing.
# this function is responsible for the pattern of the lighting mode. Feel free to change the lighting pattern as you want.
def mode1(redIntensity, greenIntensity, blueIntensity):
    red_pwm.ChangeDutyCycle(redIntensity - 1)
    sleep(0.02)
    red_pwm.ChangeDutyCycle(0)
    sleep(0.02)
    red_pwm.ChangeDutyCycle(redIntensity - 1)
    sleep(0.02)
    red_pwm.ChangeDutyCycle(0)
    sleep(0.02)
    green_pwm.ChangeDutyCycle(greenIntensity - 1)
    sleep(0.02)
    green_pwm.ChangeDutyCycle(0)
    sleep(0.02)
    green_pwm.ChangeDutyCycle(greenIntensity - 1)
    sleep(0.02)
    green_pwm.ChangeDutyCycle(0)
    sleep(0.02)
    blue_pwm.ChangeDutyCycle(blueIntensity - 1)
    sleep(0.02)
    blue_pwm.ChangeDutyCycle(0)
    sleep(0.02)
    blue_pwm.ChangeDutyCycle(blueIntensity - 1)
    sleep(0.02)
    blue_pwm.ChangeDutyCycle(0)
    sleep(0.02)
try:
    while True:                                                                              #the beginning of the main program.
        database = firebase.database()                                             #take an instance from the firebase database which is pointing to the root directory of your database.
        RGBControlBucket = database.child("RGBControl")                            #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
        powerState = RGBControlBucket.child("powerState").get().val()                        #read the power state value from the tag "powerState" which is a node inside the database.
#        print("power state is: " + str(powerState))
                                                                                             # if the "powerState" variable value is equal to "true"
        if "true" in powerState.lower():
            database = firebase.database()                                         #take an instance from the firebase database which is pointing to the root directory of your database.
            RGBControlBucket = database.child("RGBControl")                        #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
            redLightIntensity = RGBControlBucket.child("redLightIntensity").get().val()  #read the red LED intensity value from the tag "redLightIntensity" which is a node inside the database then store that value inside the "redLightIntensity" variable.
            
#            print("red Light Intensity is: " + str(redLightIntensity))
            database = firebase.database()                                         #take an instance from the firebase database which is pointing to the root directory of your database.
            RGBControlBucket = database.child("RGBControl")                        #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
            blueLightIntensity = RGBControlBucket.child("blueLightIntensity").get().val()  #read the blue LED intensity value from the tag "blueLightIntensity" which is a node inside the database then store that value inside the "blueLightIntensity" variable.
            
#            print("blue Light Intensity is: " + str(blueLightIntensity))
            database = firebase.database()                                         #take an instance from the
#firebase database which is pointing to the root directory of your database.
            RGBControlBucket = database.child("RGBControl")                        #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
            greenLightIntensity = RGBControlBucket.child("greenLightIntensity").get().val()  #read the green LED intensity value from the tag "greenLightIntensity" which is a node inside the database then store that value inside the "greenLightIntensity" variable.
            
#            print("green Light Intensity is: " + str(greenLightIntensity))
            database = firebase.database()                                         #take an instance from the firebase database which is pointing to the root directory of your database.
            RGBControlBucket = database.child("RGBControl")                        #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
            lightPresetMode = RGBControlBucket.child("lightMode").get().val()  #read the light preset mode value from the tag "lightMode" which is a node inside the database then store that value inside the "lightPresetMode" variable.
            
#            print("light preset mode is: " + str(lightPresetMode))
            #           if the variable "lightPresetMode" value is equal to "mode6", call the mode6 function.
            if "mode6" in lightPresetMode.lower():
                mode6(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
            #           if the variable "lightPresetMode" value is equal to "mode5", call the mode5 function.
            elif "mode5" in lightPresetMode.lower():
                mode5(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
            #           if the variable "lightPresetMode" value is equal to "mode4", call the mode4 function.
            elif "mode4" in lightPresetMode.lower():
                mode4(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
            #           if the variable "lightPresetMode" value is equal to "mode3", call the mode3 function.
            elif "mode3" in lightPresetMode.lower():
                mode3(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
            #           if the variable "lightPresetMode" value is equal to "mode2", call the mode2 function.
            elif "mode2" in lightPresetMode.lower():
                mode2(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
            #           if the variable "lightPresetMode" value is equal to "mode1", call the mode1 function.
            elif "mode1" in lightPresetMode.lower():
                mode1(int(redLightIntensity), int(greenLightIntensity), int(blueLightIntensity))
    #                   if the variable "lightPresetMode" value is not equal to any of the above values, print "DAMN, the power state is: false" on the terminal for debugging purposes.
        else:
            print("DAMN, the power state is: " + powerState)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    red_pwm.stop() # stop red PWM
    blue_pwm.stop() # stop blue PWM
    green_pwm.stop() # stop green PWM
    GPIO.cleanup() # cleanup all GPIO