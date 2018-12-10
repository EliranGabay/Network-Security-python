#eliran gabay
import socket
UDP_PORT = 12321
try:
    sock = socket.socket()
    print("Socket successfully created" + "\r\n")
except socket.error as error:
    print("Socket creation failed(error number:" + error.message + ")" + "\r\n")
sock.bind(('', UDP_PORT))
print("Socket binded to %s" % UDP_PORT+"\r\n")
sock.listen(5)
while True:
    client, addr = sock.accept()
    print("Got connection from", addr)
    client.send("You successfully connecting" + "\r\n")
    data = client.recv(1024)
    print(data, addr)
    client.close()
