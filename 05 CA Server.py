import socket
import random

random.seed()
i = 0
quotes = [
    "'At the end of the day, if I can say I had fun, it was a good day.'",
    "'Every day may not be good, but there's something good in every day.'",
    "'We don't have a great day, we make it a great day.'",
    "'A good day is a good day; a bad day is a good story.'",
    "'Either you run the day or the day runs you.'" ]

sSocket = socket.socket()
while 1:
    cPort = int(input("Port number to bind to: "))
    bound = ("", cPort)
    sSocket.bind(bound)

    sSocket.listen()
    cSocket, cAdd = sSocket.accept()
    print("Recieved connection from client", cAdd)

    message = ""
    while 1:
        data = cSocket.recv(4096)
        if not data:
            break
        message += data.decode("ascii")

    index = random.randint(0, 4)
    response = quotes[index]
    cSocket.sendall(response.encode("ascii"))
    cSocket.close()
    print()
