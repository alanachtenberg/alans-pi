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
	print("setting pin 7 to PWM OUT\n")
	GPIO.setup( 7, GPIO.OUT, initial=GPIO.LOW)
	p=GPIO.PWM(7,50)
	p.start(10)
	print("success\n")
	time.sleep(3)
	while(x>0):
			if(x<101):
				print("flash time \n", x)
				p.ChangeDutyCycle(x)
				time.sleep(.1)
			else:
				p.stop()
 
	print("clean up\n")
	GPIO.cleanup()
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.") 
