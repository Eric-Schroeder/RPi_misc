#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os 

# Script for power button on Raspberry Pi.
# In power off state (still plugged in),
# the RPi will boot if GPIO3 is shorted to ground.
# Add this to /etc/rc.local to run on boot. (python3 /path/to/shutdown.py &)
# **** DON'T FORGET THE '&' ****

switch = 3
switch_led = 4

GPIO.setmode(GPIO.BCM)

# Switch input
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Turn off GPIO 14
# This pin is connected to the hard drive indicator
# If nothing is connected to this pin you can ignore
GPIO.setup(14, GPIO.IN)

# Turn on switch led
GPIO.setup(switch_led, GPIO.OUT)
GPIO.output(switch_led, 1)

try:
    GPIO.wait_for_edge(3, GPIO.FALLING)

except KeyboardInterrupt:
    print('KeyboardInterrupt')

except Exception as err:
    print(err)

finally:
    GPIO.output(4, 0)
    print('shutting down...')
    GPIO.cleanup()
    os.system('sudo shutdown -h now')
