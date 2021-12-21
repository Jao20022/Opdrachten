import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("GPIO morse code")


def pulse(pin_nr, high_time, low_time):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    # copieer hier je implementatie van pulse


def morse(pin_nr, dot_length, text):
    for i in text:
        if i == ' ':
            GPIO.output(pin_nr, GPIO.LOW)
            time.sleep(dot_length)
        else:
            GPIO.output(pin_nr, GPIO.HIGH)
            if i == '-':
                time.sleep(dot_length * 3)
            elif i == '.':
                time.sleep(dot_length)
        GPIO.output(pin_nr, GPIO.LOW)
        time.sleep(dot_length)

    """
    Laat de text horen als morse code.
    De pin_nr is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """
    # implementeer deze functie


led = 18
GPIO.setup(led, GPIO.OUT)
morse(18, 0.2, ".--. -.-- - .... --- -.")

