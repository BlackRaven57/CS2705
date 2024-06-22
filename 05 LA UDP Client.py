import socket

cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketAddress = ("127.0.0.1", 2000)
message = "What time is it?"

cSocket.sendto(message.encode("ascii"), socketAddress)
data, sAddress = cSocket.recvfrom(4096)
print("Recieved response from", sAddress)
print("Server time:", data.decode("ascii"))
