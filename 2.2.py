import RPi.GPIO as GPIO
import time
import random

dacs = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dacs,GPIO.OUT)
number=[]
for i in range(0, len(dacs)):
    number.append(random.randint(0,1))
#number=[0,0,0,0,0,0,0,1] 
#2
#number = [1,1,1,1,1,1,1,1]
#255
#number = [0,1,1,1,1,1,1,1]
#127
#number = [0,0,1,1,1,1,1,1]
#64
#number = [0,0,0,1,1,1,1,1]
#32
#number = [0,0,0,0,0,1,0,1]
#5
#number = [0,0,0,0,0,0,0,0]
#0
#number = [1,0,0,0,0,0,0,0,0]
#256
for i in range((len(dacs))):
    GPIO.output(dacs[i],number[i])
time.sleep(10)
for i in range(len(dacs)):
    GPIO.output(dacs[i],0)
GPIO.cleanup()
