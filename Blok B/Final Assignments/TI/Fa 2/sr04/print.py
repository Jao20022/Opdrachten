import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
print("sr04 print")

sr04_trig = 20
sr04_echo = 21
micros = 1 / 1000000

GPIO.setup(sr04_trig, GPIO.OUT)
GPIO.setup(sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def sr04(trig_pin, echo_pin):
    """
    Return the distance in cm as measured by an SR04
    that is connected to the trig_pin and the echo_pin.
    These pins must have been configured as output and input.s
    """

    # send trigger pulse
    # inplement this step
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(10 * micros)
    GPIO.output(trig_pin, GPIO.LOW)
    # wait for echo high and remember its start time
    # inplement this step
    while True:
        if (GPIO.input(echo_pin)):
            moment1 = time.time()
            break

    # wait for echo low and remember its end time
    # inplement this step
    while True:
        if not (GPIO.input(echo_pin)):
            moment2 = time.time()
            break
    # calculate and return distance
    tijd = (moment2 - moment1)
    print(tijd)
    geluid_snelheid = 340.29
    afstand = round(((geluid_snelheid*tijd)*100)/2)
    # inplement this step
    return afstand


while True:
    print(sr04(sr04_trig, sr04_echo))
    time.sleep(0.5)
