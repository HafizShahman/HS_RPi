
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

from telepot.loop import MessageLoop


GPIO.setmode(GPIO.BCM)



TRIG = 18

ECHO = 17



print ('Distance Measurement In Progress')



GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)



GPIO.setwarnings(False)

GPIO.output(TRIG, False)

print ('Waiting For Sensor To Settle')

time.sleep(2)



globalMessageNew = 0

globalMessage = 0












def sendMessage(globalMessage):

global telegramText

global chat_id

global showMessage



if globalMessage == 1:

bot.sendMessage(chat_id, 'Rubbish: FULL!!!')



elif globalMessage == 2:

bot.sendMessage(chat_id, 'Rubbish: MEDIUM!!')



elif globalMessage == 3:

bot.sendMessage(chat_id, 'Rubbish: LOW!')

def mainprogram():

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)



while GPIO.input(ECHO)==0:

pulse_start = time.time()



while GPIO.input(ECHO)==1:

pulse_end = time.time()



pulse_duration = pulse_end - pulse_start



global distance

distance = pulse_duration * 17150

distance = round(distance)



global chat_id

global globalMessage

global globalMessageNew

print('Distance:', distance)







if distance <= 10:
globalMessage = 1

if globalMessageNew != globalMessage:

  sendMessage(globalMessage)

  globalMessageNew = globalMessage



else:

globalMessageNew = globalMessage

elif distance <= 20 and distance > 10:

globalMessage = 2

if globalMessageNew != globalMessage:

  sendMessage(globalMessage)

  globalMessageNew = globalMessage



else:

globalMessageNew = globalMessage

elif distance <= 28 and distance > 20:

globalMessage = 3

if globalMessageNew != globalMessage:

  sendMessage(globalMessage)

 globalMessageNew = globalMessage



else:

         globalMessageNew = globalMessage





time.sleep(10)

def handle(msg):
global telegramText

global chat_id

global showMessage

 global distance

chat_id = msg['chat']['id']

telegramText = msg['text']



print('Message received from ' + str(chat_id))

if telegramText == '/start':
bot.sendMessage(chat_id, 'Welcome to FAZDUSTBIN')

bot.sendMessage(chat_id, 'Location: SHAZ RESORT, PULAU TINGGI MERSING, JOHOR’)

while True:

           main()

bot = telepot.Bot(' 1352974784:AAETpsuwTig8cFTWq08rsAxlB-kfkd7_4MU’)

Bot.message_loop(handle)


while 1:

time.sleep(10)
