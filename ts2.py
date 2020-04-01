import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('ts2_ListenPort', type=int, help='Top Server Port Number')
args = parser.parse_args()
tsPORT = args.ts2_ListenPort # Top Level Server Port Number.


def topServer():

    # Preprocess and create a dictionary.

    f = open("PROJ2-DNSTS2.txt", "r")
    dictionary = {}
    for x in f:
        x = x.strip()
        word = x.split(' ')
        dictionary[word[0]] = x
    f.close()

    print(dictionary)

    # Creating socket and making all the necessary connections.

    topSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portBinding = ('', tsPORT)
    topSocket.bind(portBinding)
    topSocket.listen(5)
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)

    print("TS2 is running on Hostname: " + hostName)
    print("TS2 is running on IP Address: " + ipAddress)

    clientSocket, address = topSocket.accept()
    print('Got a connection request from: ' , address)
    
    while True:
        data = clientSocket.recv(1024).decode('utf-8').strip()
        print("Message Received: " + data)
        if not data:
            break
        if data in dictionary:
            print("Data in dictionary.")
            res = dictionary.get(data)
            clientSocket.sendall(res.encode('utf-8'))
        else:
            print("Data not in dictionary.")
            
    clientSocket.close()
    topSocket.close()
    exit()

t1 = threading.Thread(name='topServer', target=topServer)
t1.start()
exit()
