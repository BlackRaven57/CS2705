import socket

sAdd = input("IP Address of server: ")
sPort = int(input("Port number of server: "))

cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketAdd = (sAdd, sPort)
message = "What is the Quote of the Day?"
cSocket.sendto(message.encode("ascii"), socketAdd)

quote, sAdd = cSocket.recvfrom(4096)
print("Revieved response from", sAdd)
print("Quote of the Day:", quote.decode("ascii"))
