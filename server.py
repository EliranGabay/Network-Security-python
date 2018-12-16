#eliran gabay 203062831
from scapy.all import *
UDP_PORT = 12321
UDP_LOCALHOST = "127.0.0.1"
# String Xor
def strXor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
# Calculates e (Task_2)
def Cal_e(data):
    numOfPack = len(data)
    e = ""
    for x in range(numOfPack-1):
        if e =="":
            e = data[x]
        else:
            e = strXor(e,data[x+1])
    return e
# Receive data from client, check and build the Packets
def readPacketsBuild(d):
    message=[]
    count = 0
    flag = True
    while True:
        Packets, addr = UDPSock.recvfrom(1024)
        data = Packets.split('#')
        seqPack = int(data[0])
        totalPack = int(data[1])
        message.append(data[2])
        e = data[3]
        if seqPack == count:
            count+=1
            if flag:
                flag = True
        else:
            count = seqPack+1
            flag = False
        if totalPack == seqPack+1:
            break
    return message, addr, e, flag
#Build full message
def buildMessage(meg):
    return ''.join(meg)
# Create and connect UDP network service
try:
    UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPSock.bind((UDP_LOCALHOST, UDP_PORT))
    print "UDP server successful run"
except socket.error as error:
    print error
    sys.exit()
# Get messages from clients
while True:
    print "Waiting for client..."
    d, addr = UDPSock.recvfrom(1024)
    meg, client, e, flag = readPacketsBuild(d)
    if not flag:
        e1 = Cal_e(meg)
        missdata = strXor(e,e1)
        print missdata
        meg.insert(int(d),missdata)
    print str(datetime.now().time())+" Message from:",client,">",buildMessage(meg)
    UDPSock.sendto("The message received "+str(datetime.now().time()), addr)