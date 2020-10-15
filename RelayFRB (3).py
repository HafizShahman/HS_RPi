import RPi.GPIO as GPIO
import time
import pyrebase

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)






config = {
  "apiKey": "AIzaSyAD_n2A5-R0yguKbVG87PvCmVvwGejg5m0",
  "authDomain": "smart-door-3ab68",
  "databaseURL": "https://smart-door-3ab68.firebaseio.com",
  "storageBucket": "smart-door-3ab68.appspot.com"
}
firebase = pyrebase.initialize_app(config)  


global count
global mininterval
global starttime
global flow

global runtime

global db


starttime = 0
SleepTimeL = 10
       
def stream_handler(post):
    print(post["data"])
    global db
    global status

    dat = db.child("Lock").child("status").get()
    print (dat.val())
    status = dat.val()
    if(status == "LOCK"):
        print ("Door Lock")
        GPIO.output(18, GPIO.HIGH)
        
    else:
        print ("Door Un-Lock!!!")
        GPIO.output(18, GPIO.LOW)


    
    
        
    
def main():
    global db
    db = firebase.database()
    test = db.child("Lock").child("status").stream(stream_handler)       

main()


while True:
    try:

        
        time.sleep(1)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
