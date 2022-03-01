import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

GPIO.output(25,1)
GPIO.output(1,1)
GPIO.output(20,1)
GPIO.output(6,1)
GPIO.output(24,1)
GPIO.output(7,1)

