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
    ts2Binding = (ts2Hostname, ts2PORT)

    ts1Socket.connect(ts1Binding)
    # ts1Socket.sendall("Hello from LS".encode('utf-8'))
    ts2Socket.connect(ts2Binding)
    # ts2Socket.sendall("Hello from LS".encode('utf-8'))

    lsBinding = ('', lsPORT)
    lsSocket.bind(lsBinding)
    lsSocket.listen(5)

    ts1Socket.settimeout(1)
    ts2Socket.settimeout(1)

    clientSocket, address = lsSocket.accept()
    print('Got a connection request from: ' , address)

    while True:
        data = clientSocket.recv(1024).decode('utf-8').strip()
        if not data:
            break
        print("Received from client: " + data)
        
        ts1Socket.sendall(data.encode('utf-8'))
        ts2Socket.sendall(data.encode('utf-8'))

        try:
            dataTS1 = ts1Socket.recv(1024).decode('utf-8')
            print("Data from TS1: " + dataTS1)
            clientSocket.sendall(dataTS1.encode('utf-8'))
        except socket.timeout:
            print("No Response from TS 1, trying TS 2.")
            try:
                dataTS2 = ts2Socket.recv(1024).decode('utf-8')
                print("Data from TS2: " + dataTS2)
                clientSocket.sendall(dataTS2.encode('utf-8'))
            except socket.timeout:
                print("No Response from TS 2. Responding with Error.")
                clientSocket.sendall(data + " - Error:HOST NOT FOUND".encode('utf-8'))      


    lsSocket.close()
    ts1Socket.close()
    ts2Socket.close()
    exit()

t1 = threading.Thread(name='loadBalancer', target=loadBalancer)
t1.start()
exit()