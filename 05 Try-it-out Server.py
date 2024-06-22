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

while i == 0:
    sSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cPort = int(input("Port number to bind to: "))
    bound = ("", cPort)
    sSocket.bind(bound)

    data, cAdd = sSocket.recvfrom(4096)
    print("Recieved request from clinent", cAdd)

    index = random.randint(0, 4)
    message = quotes[index]
    sSocket.sendto(message.encode("ascii"), cAdd)
    print()
