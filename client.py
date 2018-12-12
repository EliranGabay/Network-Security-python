#eliran gabay
import socket
import random
import string
import time
# Create and connect UDP network Client
UDP_PORT = 12321
UDP_LOCALHOST = '127.0.0.1'
try:
    UDPCSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPCSock.bind((UDP_LOCALHOST, 8080))
except socket.error as error:
    print error
# Send message to UDP server
text = "".join([random.choice(string.letters) for i in xrange(3)])
timeS = time.localtime().tm_sec
while True:
    if (timeS+3) == time.localtime().tm_sec:
        UDPCSock.sendto(text, (UDP_LOCALHOST, UDP_PORT))
        print(UDPCSock.recvfrom(1024),timeS)
        timeS = time.localtime().tm_sec
    if (timeS+3) >= 60:
        timeS = time.localtime().tm_sec