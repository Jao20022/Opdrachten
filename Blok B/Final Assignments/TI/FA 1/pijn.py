import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

servo = 25
GPIO.setup(servo,GPIO.OUT)


def pulse(pin, delay1, delay2):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay2)

while True:
    pulse(servo, 0.0005,0.1)

    pulse(servo, 0.0024,0.1)
