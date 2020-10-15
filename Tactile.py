import os
from time import sleep
import random
 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN,pull_up_down=GPIO.PUD_UP)

import pyrebase 
##pyrebase bisa di download di https://github.com/thisbejim/Pyrebase.
##untuk mendapatkan config file atau kode bisa didapatkan pada opsi Web di Firebase
##jangan lupa untuk menginstal beberapa requriment yang diperlukan.
##pastikan baca README yang ada atau require text.

config = {
  "apiKey": "AIzaSyAD_n2A5-R0yguKbVG87PvCmVvwGejg5m0",
  "authDomain": "smart-door-3ab68",
  "databaseURL": "https://smart-door-3ab68.firebaseio.com",
  "storageBucket": "smart-door-3ab68.appspot.com"
}
firebase 	= pyrebase.initialize_app(config)
db = firebase.database()



##mengupload data di tabel yang sudah di tentukan
lock = ("LOCK")
unlock = ("UNLOCK")


while True:
    if (GPIO.input(5) == False):
        db.child("Users").child("Door").child("fypjun2020").child("status").set(lock)
        print ("LOCK")
        sleep(3)
    else:
        print ("UNLOCK")
        db.child("Users").child("Door").child("fypjun2020").child("status").set(unlock)
        sleep(3)

