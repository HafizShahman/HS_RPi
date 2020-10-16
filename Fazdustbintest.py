@@ -1,80 +0,0 @@
import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
#declare pin
TRIG = 18
ECHO = 17
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(eCHO,GPIO.IN)
try:
    while True:
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        time.sleep(1800)                         #Delay of 2 seconds

        GPIO.output(TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                      #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                 #Set TRIG as LOW

        while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()            #Saves the last known time of LOW pulse

        while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()              #Saves the last known time of HIGH pulse

        pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)

        if distance >= 20:
            stat = "LOW"

        if distance < 20 and distance > 5 :
            stat = "MEDIUM"

        if distance <= 5:
            stat = "HIGH"

        def action(msg):
            chat_id = msg['chat']['id']
            command = msg['text']
            print 'Received: %s' % command
            if 'check' in command:
                message = "Check Bin"

            message = "Dustbin 1 : " + stat
            telegram_bot.sendMessage (chat_id, message)

        telegram_bot = telepot.Bot('1352974784:AAETpsuwTig8cFTWq08rsAxlB-kfkd7_4MU')
        print (telegram_bot.getMe())
        MessageLoop(telegram_bot, action).run_as_thread()
        print 'Up and Running....'
        while 1:
            time.sleep(10)

except KeyboardInterrupt:
    GPIo.cleanup()
