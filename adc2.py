import RPi.GPIO as GPIO
import time
dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def num2pins(pins, value):
    GPIO.output(pins, [int(i) for i in bin(value)[2:].zfill(8)])

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]
def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

def adc():
    value = 0
    direction = 1
    for i in range(8):
        delta = 2 ** (8 - i - 1)
        value += delta * direction
        voltage = value / levels * maxVoltage
        if i == 7:
            print(value, voltage, direction)
        num2pins(dac, value)
        time.sleep(0.001)
        direction = -1 if (GPIO.input(comparator) == 0) else 1
    return(value)
try:
    GPIO.output(troykaModule, 1)
    while True:
        adc()


except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.cleanup()
    print("GPIO cleanup")