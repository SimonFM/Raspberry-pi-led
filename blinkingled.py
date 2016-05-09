import RPi.GPIO as GPIO
import time

#sets up the pi to make an output on GPIO pin 18
def setupOurPi():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(18,GPIO.OUT)
  
  
  
# This simple while loop will make an LED flash on and off
def makeLEDBlink():
  while(True):
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)
    GPIO.output(18,GPIO.HIGH)
    print "LED on"
    time.sleep(1)
    
# call our set up method
setupOurPi()

# call our blink method
makeLEDBlink()