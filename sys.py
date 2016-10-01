import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)	#so no interputions
GPIO.setmode(GPIO.BOARD)#id type of board check the docs
GPIO.setup(3,GPIO.OUT)	#channel:pin to LED
GPIO.output(3,0)	#Init staet of LED is off
GPIO.setup(11,GPIO.IN)	#read from the pir sensor
print "begin test"
time.sleep(2)		#this is to caibrate the infrared sensor
print "done calibrating...begin:"
while True:
	state = GPIO.input(11)		#read from the pir
	if state == 1:			#if detected	
		GPIO.output(3,1)	#turn on LED
		print "INTRUDER!"	
		time.sleep(.1)
		
	elif state == 0:
		GPIO.output(3,0)
		print "Null"
		time.sleep(.1)
""" Run this to test if connection is good: Blinking LED
while True:
	GPIO.output(3,1)
	time.sleep(1)
	GPIO.output(3,0)
	time.sleep(1)
"""
