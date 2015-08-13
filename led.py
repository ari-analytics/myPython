import RPi.GPIO as GPIO
import time

ledPin19 = 19
ledPin26 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin19,GPIO.OUT)
GPIO.setup(ledPin26,GPIO.OUT)

# Initial state for LEDs:
GPIO.output(ledPin19,GPIO.LOW)
GPIO.output(ledPin26,GPIO.LOW)

print ("Here we go! Press CTRL+C to exit")

try:
	while 1:
		GPIO.output(ledPin19,GPIO.HIGH)
		GPIO.output(ledPin26,GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(ledPin26,GPIO.HIGH)
		GPIO.output(ledPin19,GPIO.LOW)
		time.sleep(0.1)
		
except KeyboardInterrupt:
	GPIO.cleanup()


