import socket
import random
import string
import time
sock=socket.socket()
UDP_PORT = 12321
UDP_LOCALHOST = "127.0.0.1"
sock.connect((UDP_LOCALHOST,UDP_PORT))
text="".join([random.choice(string.letters) for i in xrange(3)])
timeS=time.localtime().tm_sec
while True:
    if(timeS+3)==time.localtime().tm_sec:
        sock.send(text)
        print("time:", timeS)
        timeS=time.localtime().tm_sec
    if (timeS+3)>=60:
        timeS=time.localtime().tm_sec
print(sock.recv(1024))
sock.close()