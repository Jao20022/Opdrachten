import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("input copy")

led = 18
on_switch = 23
off_switch = 24

GPIO.setup(led, GPIO.OUT)
GPIO.setup(on_switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(off_switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
on = False
while True:
    if (GPIO.input(on_switch)):
        on = True
        print('on')
    elif (GPIO.input(off_switch)):
        on = False
        print('off')
    else:
        pass
    if on:
        GPIO.output(led, GPIO.HIGH)
    else: GPIO.output(led, GPIO.LOW)
    time.sleep(0.1)
