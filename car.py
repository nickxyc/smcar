import RPi.GPIO as GPIO
#from remotecontrol import *
from Carclass import Car
import time
from Carclass import dangerous
import socket
import threading
'''小车的初始化程序，小车设备的主程序，各个模块的枢纽，也是面向用户的接口，用户可以通过这个模块来实现
对小车的控制。未来友GUI计划，但是不保证可实现性'''
'''
version 1.0.0
auther nick
'''
caraction = Car()
dangerous = dangerous()
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

def remote():
    a = threading.Thread(target=dangerous.check)
    a.start()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind('127.0.0.1',9999)
    s.listen(5)
    print('等待连接')
    while True:
        sock,addr = s.accept()
        d = threading.Thread(target=deal,args=(sock,addr,caration))
        d.start()
def deal(sock,addr,caration):
    '''
    处理来自网络的命令将其变成小车的动作
    :return:
    '''
    recvmessage = sock.recv(1024).decode('utf-8')
    if recvmessage == 'F':
        caration.forward()
    if recvmessage == 'L':
        caration.turn_left()
    if recvmessage == 'R':
        caration.trun_right()
    if recvmessage == 'S':
        caration.stop()
    if recvmessage == 'B':
        caration.back()
