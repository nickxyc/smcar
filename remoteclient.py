import socket
from config import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,PORT))
while True:
    print('你想作什么')
    sendmessage = input()
    if sendmessage == 'w':
        s.send(b'F')
    if sendmessage == 's':
        s.send(b'S')
    if sendmessage == 'a':
        s.send(b'L')
    if sendmessage == 'd':
        s.send(b'R')