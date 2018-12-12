#eliran gabay
import socket
import random
import string
import time
import datetime

#Split the data to Packets
def SplitPack(data):
    # Get the size of data
    dataSize = len(data.encode('utf-8'))
    numOfPack = (dataSize/100)+1
    if dataSize>10:
        data=[data[i:i+100] for i in range(0, dataSize, 100)]
    return data

# Create and connect UDP network Client
UDP_PORT = 12321
UDP_LOCALHOST = '127.0.0.1'
try:
    UDPCSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPCSock.bind((UDP_LOCALHOST, 8080))
except socket.error as error:
    print error
    # Send message to UDP server every 3 sec
timeS = time.localtime().tm_sec
while True:
    text = "".join([random.choice(string.letters) for i in xrange(250)])
    text=SplitPack(text)
    if (timeS+3) == time.localtime().tm_sec:
        for data in text:
            UDPCSock.sendto(data, (UDP_LOCALHOST, UDP_PORT))
            UDPCSock.sendto(str(text.index(data)), (UDP_LOCALHOST, UDP_PORT))
        print datetime.datetime.now().time(), UDPCSock.recvfrom(1024)
        timeS = time.localtime().tm_sec
    if (timeS+3) >= 60:
        timeS = time.localtime().tm_sec