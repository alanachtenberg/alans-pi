#turns off pins 5 and 7
try:
	import time
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	print("import and set pin mode to board success!")
	print("setting 5 an 7 to off\n")
	GPIO.setup( 5, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup( 7, GPIO.OUT, initial=GPIO.LOW)
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.") 
