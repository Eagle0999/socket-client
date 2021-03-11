#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
print('Client started!!!')
sock = socket.socket()
sock.connect(('localhost', 9090))
print('Client is sending the message to Server:  hello, world!')
sock.send('hello, world!'.encode())

data = sock.recv(1024).decode()
print('Client recieved the message from Server: ',data)
sock.close()