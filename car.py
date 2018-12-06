import RPi.GPIO as GPIO
from remotecontrol import *
#from Carclass import Car
import time
#from Carclass import dangerous
'''小车的初始化程序，小车设备的主程序，各个模块的枢纽，也是面向用户的接口，用户可以通过这个模块来实现
对小车的控制。未来友GUI计划，但是不保证可实现性'''
'''
version 1.0.0
auther nick
'''
try:
    '''设置树莓派上GPIO接口的初始状态，并且实例对象'''
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
    print('选择模式')
    print('1.遥控模式')
    choice = input()
    if choice == '1':
        remote()
finally:
    time.sleep(1)
    GPIO.cleanup()
