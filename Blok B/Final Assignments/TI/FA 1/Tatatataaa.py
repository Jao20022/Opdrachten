import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

GPIO.setup(18, GPIO.OUT)


def kort():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.2)


def lang():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.2)


while True:
    kort()
    kort()
    kort()
    lang()
'''
Maak een programma (dus: kopieer en pas 
aan!) dat de LED kort-kort-kort-lang laat 
blinken. 
'''
