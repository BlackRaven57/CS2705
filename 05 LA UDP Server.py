import socket
import datetime

sSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
boundAdd = ("", 2000)
sSocket.bind(boundAdd)

data, cAddress = sSocket.recvfrom(4096)
print("Recieved request from client", cAddress)

now = datetime.datetime.now()
message = now.isoformat()
sSocket.sendto(message.encode("ascii"), cAddress)
