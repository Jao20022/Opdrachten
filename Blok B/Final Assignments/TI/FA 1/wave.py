import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("servo wave")


def pulse(pin, delay1, delay2):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay2)
    # copieer hier je implementatie van de pulse functie


def servo_pulse(pin_nr, position):
    print(position)
    x = (position * 0.000025) + 0.0005
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(0.002)
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.
    
    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms
    
    Before this function is called, 
    the gpio pin must be configured as output.
    """

    # implementeer deze functie


servo = 25
GPIO.setup(servo, GPIO.OUT)

while True:
    for i in range(0, 100, 1):
        servo_pulse(servo, i)
    time.sleep(0.5)
    for i in range(100, 0, -1):
        servo_pulse(servo, i)
