#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
command = 'Получить файл'
#command = 'Отправить файл'
filename = 'test1.txt'
print('Client started!!!')
sock = socket.socket()
sock.connect(('192.168.56.101', 9090))
print('Client is sending the message to Server:  hello, world!')
#sock.send('hello, world!'.encode())
if command =='Получить файл':
    sock.send((command+','+filename).encode('UTF-8'))
    data = sock.recv(1024).decode('UTF-8')
    file = open(filename,'w')
    file.write(data)
    file.close()
    print('Client recieved the message from Server: ',data)
    
if command =='Отправить файл':
    file = open(filename,'r')
    content = file.read()
    sock.send((command+','+filename+','+content).encode('UTF-8'))
    file.close()
    
    data = sock.recv(1024).decode('UTF-8')
    print('Client recieved the message from Server: ',data)
    
sock.close()

