import socket

sSocket = socket.socket()
boundAdd = ("", 3000)
sSocket.bind(boundAdd)

sSocket.listen()
cSocket, cAdd = sSocket.accept()
print("Recieved connection from client", cAdd)

message = ""
while 1:
    data = cSocket.recv(4096)
    if not data:
        break
    message += data.decode("ascii")

print("Recieved message:", message)
response = message.upper()
cSocket.sendall(response.encode("ascii"))
cSocket.close()
