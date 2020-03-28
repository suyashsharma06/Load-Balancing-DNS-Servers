import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('ts1_ListenPort', type=int, help='Top Server Port Number')
args = parser.parse_args()
tsPORT = args.ts1_ListenPort # Top Level Server Port Number.


def topServer():

    # Preprocess and create a dictionary.

    f = open("PROJ2-DNSTS1.txt", "r")
    dictionary = {}
    for x in f:
        x = x.strip()
        word = x.split(' ')
        dictionary[word[0]] = x
    f.close()

    print(dictionary)

    # Creating socket and making all the necessary connections.

    topSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("top Socket 1 has been created.")
    portBinding = ('', tsPORT)
    topSocket.bind(portBinding)
    topSocket.listen(5)
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print("Socket Creation on Top Server 1 is now complete.", ipAddress)

    clientSocket, address = topSocket.accept()
    print("got a connection request from ", address)
    
    while True:
        data = clientSocket.recv(1024).decode('utf-8').strip()
        print("Received " + data + " from Client.")
        if not data:
            break
        if data in dictionary:
            res = dictionary.get(data)
            clientSocket.sendall(res.encode('utf-8'))
        else:
            break

    clientSocket.close()
    topSocket.close()
    exit()

t1 = threading.Thread(name='topServer', target=topServer)
t1.start()
exit()
