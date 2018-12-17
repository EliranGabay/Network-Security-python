import string
from scapy.all import *
UDP_PORT = 12321
UDP_LOCALHOST = '127.0.0.1'
#Split the data to Packets
def SplitPack(data):
    dataSize = len(data.encode('utf-8'))
    numOfPack = (dataSize/100)
    if dataSize>100:
        data=[data[n:n + 100] for n in range(0, dataSize, 100)]
        udp_packets = []
        for x in range(numOfPack):
            udp_packets.append(str(x)+"#"+str(numOfPack)+"#"+data[x])
    return udp_packets,data
# String Xor
def strXor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
# Calculates e (Task_2)
def Cal_e(data):
    numOfPack = len(data)
    d = random.randint(0,numOfPack-1)
    e = ""
    for x in range(numOfPack-1):
        if e =="":
            e = data[x]
        else:
            e = strXor(e,data[x+1])
    return e, d
#Create and connect UDP network Client
try:
    UDPCSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPCSock.bind((UDP_LOCALHOST, random.randint(1000,8888)))
except socket.error as error:
    print error
    sys.exit()
#Send message to UDP server every 3 sec
text = "".join([random.choice(string.letters) for i in xrange(400)])
Pack,data = SplitPack(text)
e, d = Cal_e(data)
while True:
    UDPCSock.sendto(str(d),(UDP_LOCALHOST,UDP_PORT))
    for i in range(len(Pack)):
        if i is not d:
            print "send:"+Pack[i]+"#"+str(e)
            UDPCSock.sendto(str(Pack[i])+"#"+str(e),(UDP_LOCALHOST,UDP_PORT))
            time.sleep(0.1)
        else:
            print Pack[i]
    print UDPCSock.recv(1024)
    time.sleep(3)
