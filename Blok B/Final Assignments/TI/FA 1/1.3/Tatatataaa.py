import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

GPIO.setup(18, GPIO.OUT)

pin = 18
kort = 0.2
lang = 1

def pulse(pin_nr, high_time, low_time):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)


while True:
   pulse(pin, kort, 0.2)
   pulse(pin, kort, 0.2)
   pulse(pin, kort, 0.2)
   pulse(pin, lang, 0.2)

'''
Maak een programma (dus: kopieer en pas 
aan!) dat de LED kort-kort-kort-lang laat 
blinken. 
'''
