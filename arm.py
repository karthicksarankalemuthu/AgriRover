import RPi as GPIO
from time import sleep 


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(12, 50)

#pwm.start(0)

def moter1(angle):
	#pwm.start(0)
	duty = round(int(angle) / 18 )+ 2
	GPIO.output(12, True)
	#pwm.ChangeDutyCycle(duty)
	#pwm.stop()
	print(duty)
	
#pwm.stop()

def moter2(angle):
	#pwm.start(0)
	duty = round(int(angle) / 18 )+ 2
	GPIO.output(12, True)
	#pwm.ChangeDutyCycle(duty)
	#pwm.stop()
	print(duty)