from rpy_push import *
import RPi.GPIO as GPIO

CODE = ""

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
	if(GPIO.input(23) == 1):
		push_note(CODE, "GPIO", ":D")

GPIO.cleanup()