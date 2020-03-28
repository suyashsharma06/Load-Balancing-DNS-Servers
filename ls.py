import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('lsListenPort', type=int, help='Root Server Port Number')
parser.add_argument('ts1Hostname', type=int, help='Root Server Port Number')
parser.add_argument('ts1ListenPort', type=int, help='Root Server Port Number')
parser.add_argument('ts2Hostname', type=int, help='Root Server Port Number')
parser.add_argument('ts2ListenPort', type=int, help='Root Server Port Number')
args = parser.parse_args()


lsPORT = args.lsListenPort
ts1PORT = args.ts1ListenPort
ts2PORT = args.ts2ListenPort


def rootServer():

    # Create a socket, let Client connect, take his string, make request, wait for 10 seconds, timeout if there is no reponse from the TS and return error message.

    loadServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Load Server has been created.")
    portBinding = ('', lsPORT)
    loadServer.bind(portBinding)
    loadServer.listen(5)
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print("Socket Creation on Load Server is now complete.", ipAddress)

    clientSocket, address = loadServer.accept()
    print("got a connection request from ", address)

    errorString = " - Error:HOST NOT FOUND"

    while True:
        data = clientSocket.recv(1024).decode('utf-8').strip()
        print("Received " + data + " from Client.")
        
        


t1 = threading.Thread(name='rootServer', target=rootServer)
t1.start()
exit()