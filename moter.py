import RPi as GPIO
from time import sleep 


mo_11=13     #en_1 forword
mo_12=15     #en_1 backword
mo_21=17     #en_2 forword
mo_22=18     #en_2 backword


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(mo_11, GPIO.OUT) 
GPIO.setup(mo_12, GPIO.OUT) 
GPIO.setup(mo_21, GPIO.OUT) 
GPIO.setup(mo_22, GPIO.OUT) 


def forword():
   GPIO.output(mo_11, GPIO.HIGH)
   GPIO.output(mo_12, GPIO.LOW)
   GPIO.output(mo_21, GPIO.HIGH)
   GPIO.output(mo_22, GPIO.LOW)
   print("forword")

def backword():
   GPIO.output(mo_11, GPIO.LOW)
   GPIO.output(mo_12, GPIO.HIGH)
   GPIO.output(mo_21, GPIO.LOW)
   GPIO.output(mo_22, GPIO.HIGH)
   print("backword")

def right():
   GPIO.output(mo_11, GPIO.HIGH)
   GPIO.output(mo_12, GPIO.LOW)
   GPIO.output(mo_21, GPIO.LOW)
   GPIO.output(mo_22, GPIO.HIGH)
   print("right")

def left():
   GPIO.output(mo_11, GPIO.LOW)
   GPIO.output(mo_12, GPIO.HIGH)
   GPIO.output(mo_21, GPIO.HIGH)
   GPIO.output(mo_22, GPIO.LOW)
   print("left")   

def stop():
   GPIO.output(mo_11, GPIO.LOW)
   GPIO.output(mo_12, GPIO.LOW)
   GPIO.output(mo_21, GPIO.LOW)
   GPIO.output(mo_22, GPIO.LOW)
   print("stop")   