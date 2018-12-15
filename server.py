#eliran gabay
from scapy.all import *
UDP_PORT = 12321
UDP_LOCALHOST = "127.0.0.1"
# Create and connect UDP network service
try:
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    UDPSock.bind((UDP_LOCALHOST, UDP_PORT))
    UDPSock.listen(10)
    print "UDP server successful run"
except socket.error as error:
    print error
# Get messages from clients
while True:
    print "Waiting for client..."
    client, addr=UDPSock.accept()
    print client.getpeername()," connect to server"
    client.send("Connecting server successful".encode('utf-8'))
    while True:
        data = client.recv(1024)
        print data
        if not data:
            client.send("The massage received".encode('utf-8'))
            break
    #print datetime.now().time(), " Message from:", client, ":", data.decode('utf-8')
    client.close()
