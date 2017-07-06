#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

__program__ = 'FanControl'
__version__ = '1.2a'

def getCPUTemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=",'').replace("'C\n",''))

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

FAN = GPIO.PWM(4, 50)

FAN.start(0)

print("Starting " + __program__ + " v." + __version__)
try:
    while 1:
        cpu = float(getCPUTemp())
        if (cpu<30):
            dc = 0
        elif (cpu <40):
            dc = 55
        elif (cpu<45):
            dc = 70
        elif (cpu<50):
            dc = 80
        else :
            dc = 99
        FAN.ChangeDutyCycle(dc)
        print("PWM : " + str(dc) + "  TEMP : " + str(cpu) , end='\r')
        time.sleep(10)

except KeyboardInterrupt:
    print("Shutdown")
    pass
FAN.stop()
GPIO.cleanup()
