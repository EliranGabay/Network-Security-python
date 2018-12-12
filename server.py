#eliran gabay
import datetime
import socket

UDP_PORT = 12321
UDP_LOCALHOST = "127.0.0.1"
# Create and connect UDP network service
try:
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPSock.bind((UDP_LOCALHOST, UDP_PORT))
    print "UDP server successful run"
except socket.error as error:
    print error
# Get messages from clients
while True:
    data, client = UDPSock.recvfrom(1024)
    print datetime.datetime.now().time(), " Message from:", client, ":", data
    UDPSock.sendto("The massage received", client)
