import RPi.GPIO as GPIO
from Carclass import Car
import time
from Carclass import dangerous
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(caraction.IN3,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(caraction.IN4,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(caraction.IN1,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(caraction.IN2,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(dangerous.TRIG,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(dangerous.ECHO,GPIO.IN)
    GPIO.setup(dangerous.BEE,GPIO.OUT,initial = GPIO.HIGH)
    GPIO.setup(caraction.R_LIGHT,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(caraction.G_LIGHT,GPIO.OUT,initial = GPIO.LOW)
    GPIO.setup(caraction.B_LIGHT,GPIO.OUT,initial = GPIO.LOW)
    caraction = Car()
    dangerous = dangerous()

    caraction.forward()
    while(1):
        if dangerous.check() == 0:
            break
        
    #time.sleep(3)
    #caraction.stop()
finally:
    time.sleep(1)
    GPIO.cleanup()
