import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

GPIO.setup(25, GPIO.OUT)


def servo_pulse(pin_nr, position):
    x = (position * 0.000025) + 0.0005
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(0.002)

    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the
    specified position, and then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be
    in the range 0.5 ms .. 2.5 ms.

    Before this function is called,
    the gpio pin must have been configured as output.
    """

servo_pulse(25, 5)