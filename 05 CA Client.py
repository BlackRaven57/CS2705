import socket

sAdd = input("IP Address of server: ")
sPort = int(input("Port number of server: "))
cSocket = socket.socket()
socketAdd = (sAdd, sPort)
cSocket.connect(socketAdd)

message = "What is the Quote of the Day?"
cSocket.sendall(message.encode("ascii"))
cSocket.shutdown(socket.SHUT_WR)

quote = ""
while 1:
    data = cSocket.recv(4096)
    if not data:
        break
    quote += data.decode("ascii")

print("Revieved response from server")
print("Quote of the Day:", quote)
