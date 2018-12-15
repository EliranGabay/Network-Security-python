#eliran gabay
import string

from scapy.all import *
class UDPacket:
    def __init__(self,data,seqNum):
        self.sizePacket = len(data.encode('utf-8'))
        self.data = data
        self.seq_num = seqNum
#Split the data to Packets
def SplitPack(data):
    # Get the size of data
    dataSize = len(data.encode('utf-8'))
    numOfPack = (dataSize/100)+1
    if dataSize>10:
        data=[data[n:n + 100] for n in range(0, dataSize, 100)]
        udp_packets = []
        for x in range(numOfPack):
            udp_packets.append(UDPacket(data[x],x))
    return udp_packets
# Create and connect UDP network Client
UDP_PORT = 12321
UDP_LOCALHOST = '127.0.0.1'
try:
    UDPCSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    UDPCSock.bind((UDP_LOCALHOST, random.randint(1000,8888)))
except socket.error as error:
    print error
    sys.exit()
# Send message to UDP server every 3 sec
text = "".join([random.choice(string.letters) for i in xrange(450)])
text=SplitPack(text)
try:
    UDPCSock.connect((UDP_LOCALHOST,UDP_PORT))
    print UDPCSock.recv(1024)
except socket.error as error:
    print error
    sys.exit()
while True:
    for i in range(len(text)):
        print text[i].data
        UDPCSock.send(text[i].data.encode('utf-8'))
        UDPCSock.send(str(text[i].seq_num).encode('utf-8'))
    print datetime.now().time(), UDPCSock.recv(1024)
    time.sleep(3)
UDPCSock.close()