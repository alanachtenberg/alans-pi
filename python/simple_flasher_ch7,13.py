try:
	import Tkinter as tk
	import thread
	import time
	import RPi.GPIO as GPIO
	x=10

	def input_thread():
		global x
		while(1):
			x=int(raw_input("thread input"))
			if(x==750):
				for v in range (1,2):
					for t in range (1,50):
						x=t
						time.sleep(.15)
					for t in range (1,50):
						x=51-t
						time.sleep(.15)
			x=min(x,500)
		print("input thread exited!")
	thread.start_new_thread(input_thread,())
	GPIO.setmode(GPIO.BOARD)
	print("import and set pin mode to board success!")
	print("setting pin 5 and 7 to GPIO OUT\n")
	GPIO.setup( 5, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup( 7, GPIO.OUT, initial=GPIO.LOW)
	print("success\n")
	time.sleep(3)
	while(x>0):
			print("flash time \n", x)
			GPIO.output(7,GPIO.HIGH)
			time.sleep(.01*x)
			GPIO.output(7,GPIO.LOW)
			time.sleep(.01*x)
			if x>35:
				GPIO.output(5,GPIO.HIGH)
			else: 
				GPIO.output(5,GPIO.LOW) 
	print("clean up\n")
	GPIO.cleanup()
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.") 
