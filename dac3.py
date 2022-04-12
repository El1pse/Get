import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(22, 1000)
p.start(0)
try:
    while True:
        inputStr = int(input("Enter value"))
        dc = inputStr    
        p.ChangeDutyCycle(dc)
finally:
    p.stop()
    GPIO.cleanup()
