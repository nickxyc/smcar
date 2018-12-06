# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from Carclass import Car,dangerous
import socket
import threading
'''
小车远程控制的服务端，目的是通过网络(待定)来控制小车的行为，存在理论上的可行性项目不保证成功性
version 1.0
author nick_xyc
'''
def remote():
    caration = Car()
    dangerous = dangerous()
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


