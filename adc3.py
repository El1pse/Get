import RPi.GPIO as GPIO
import time
dac = [26,19,13,6,5,11,9,10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]
def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        for value in range(256):
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            s = value
            time.sleep(0.001)
            comparatorValue = GPIO.input(comparator)
            if comparatorValue == 0:
                print("Entered value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))
                break
        a=[]
        for i in range(8):
            if s//2 >= 1:
                a.append(1)
            if s//2 == 0:
                a.append(0)
            s = s // 2
        GPIO.output(leds,a)


except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup")