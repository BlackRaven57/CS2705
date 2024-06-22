import socket

cSocket = socket.socket()
sAdd = ("127.0.0.1", 3000)
cSocket.connect(sAdd)

message = input("Enter a message: ")
cSocket.sendall(message.encode("ascii"))
cSocket.shutdown(socket.SHUT_WR)

response = ""
while 1:
    data = cSocket.recv(4096)
    if not data:
        break
    response += data.decode("ascii")

print("Recieved response from server")
print(response)
