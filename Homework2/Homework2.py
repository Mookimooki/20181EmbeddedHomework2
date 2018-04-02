#!/usr/bin/env python

import time as time
import RPi.GPIO as GPIO

TRIG =	20
ECHO =	21
BUZZ =	22
STRT = 	23
STOP =	24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.LOW)
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.setup(STOP, GPIO.IN)
GPIO.setup(STRT, GPIO.IN)

def warnDepth(depth):
	isBuzzing = False
	gap = 0
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		
		while GPIO.input(ECHO) == False:
			pulse_start = time.time()
		while GPIO.input(ECHO) == True:
			pulse_end = time.time()
		
		pulse_duration = pulse_end - pulse_start		
		distance = pulse_duration * 17150
		distance = round(distance, 2)
		
		if distance > (depth + gap) and isBuzzing == True:
			GPIO.output(BUZZ, False)
			isBuzzing = False
			gap = 0
	
		if distance < depth and isBuzzing == False:
			GPIO.output(BUZZ, True)
			isBuzzing = True
			gap = 5
	
		if(GPIO.input(STOP) == True):
			print("end")
			GPIO.output(BUZZ, False)
			isBuzzing = False
			return
		time.sleep(0.1)

while True:
	if (GPIO.input(STRT) == True):
		print("Start:")
		warnDepth(30)
