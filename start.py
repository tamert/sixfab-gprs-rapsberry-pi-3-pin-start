import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import ‘time’ library. Allows us to use ‘sleep’

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(22, GPIO.OUT) ## Setup GPIO pin 7 to OUT

GPIO.output(22, True) ## Turn on GPIO pin 7
time.sleep(3) ## Wait

GPIO.output(22, False) ## Switch off GPIO pin 7
GPIO.cleanup()
