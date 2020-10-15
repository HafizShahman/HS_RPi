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

##mengupdate database
##db.child("Sensor1").update({"Persentasi": "200", "Level": "1020"})

##menghapus data
##db.child("users").child("Morty").remove()
##db.child("Sensor1").remove()


##mengupload data di tabel yang sudah di tentukan
lock = ("LOCK")
unlock = ("UNLOCK")


while True:
    if (GPIO.input(5) == False):
        db.child("Users").child("4VolNb6YPXYuSsGwErTxo4Baojh2").child("Tstatus").set(lock)
        print ("Hello")
        sleep(3)
    else:
        print ("Dah settle")
        db.child("Users").child("4VolNb6YPXYuSsGwErTxo4Baojh2").child("Tstatus").set(unlock)
        sleep(3)

##mengupload data dengan unique id / sembarang nama
#data = {"Persentasi": "90", "Level": "1020"}
#db.child("Sensor1").push(data)


#while True:
#    if (GPIO.input(5) == False):
#       print ("Hello")
#       sleep(3)
#    else:
#        print ("Dah settle")
#        sleep(3)

