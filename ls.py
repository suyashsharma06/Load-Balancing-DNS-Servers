import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('lsListenPort', type=int, help='Root Server Port Number')
parser.add_argument('ts1Hostname', type=str, help='Root Server Port Number')
parser.add_argument('ts1ListenPort', type=int, help='Root Server Port Number')
parser.add_argument('ts2Hostname', type=str, help='Root Server Port Number')
parser.add_argument('ts2ListenPort', type=int, help='Root Server Port Number')
args = parser.parse_args()


lsPORT = args.lsListenPort
ts1PORT = args.ts1ListenPort
ts2PORT = args.ts2ListenPort

ts1Hostname = args.ts1Hostname
ts2Hostname = args.ts2Hostname

def loadBalancer():
    errorString = " - Error:HOST NOT FOUND"

    try:
        ts1Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket Open Error: " + err)

    ts1Binding = (ts1Hostname, ts1PORT)
    ts2Binding = (ts2Binding, ts2PORT)

    ts1Socket.connect(ts1Binding)
    ts2Socket.connect(ts2Binding)

    ts1Socket.settimeout(5)
    ts2Socket.settimeout(5)

    clientConnection, address = lsSocket.accept()
    print("Got a connection request from: " + address)

    while True:
        data = clientConnection.recv(1024).decode('utf-8').stript()
        print("received from client: " + data)
        if not data:
            break
        
        try:
            ts1Socket.sendall(data.encode('utf-8'))
            ts2Socket.sendall(data.encode('utf-8'))
            dataTS1 = ts1Socket.recv(1024).decode('utf-8')
            dataTS2 = ts2Socket.recv(1024).decode('utf-8')
        except socket.timeout:
            print("We got timeout error.")

        lsSocket.sendall(errorString.encode('utf-8'))

    clientConnection.close()
    ts1Socket.close()
    ts2Socket.close()
    lsSocket.close()
    exit()

t1 = threading.Thread(name='loadBalancer', target=loadBalancer)
t1.start()
exit()