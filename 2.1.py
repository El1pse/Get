import RPi.GPIO as GPIO
import time

leds = [21,20,16,12,7,8,25,24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
for j in range(3):
    for i in range(len(leds)):
        GPIO.output(leds[i],1)
        time.sleep(0.2)
        GPIO.output(leds[i],0)
    
