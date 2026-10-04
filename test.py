#!/home/don/python/bin/python3
# by Don Bales
# on 2026-10-04

#from datetime import datetime
#from email.message import EmailMessage
import os
#from pathlib import Path
import RPi.GPIO as GPIO
#import subprocess
#import smtplib
#import sys
import time

os.system('modprobe w1-gpio')

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

channel_list = [26,20,21]
GPIO.setup(channel_list, GPIO.OUT)

RELAY1 = 26
RELAY2 = 20
RELAY3 = 21

try:
    while True:
        GPIO.output(RELAY1, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RELAY2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RELAY3, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RELAY1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RELAY2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RELAY3, GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
