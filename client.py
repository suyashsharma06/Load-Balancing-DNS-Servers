import threading
import time
import random
import socket
import argparse

# Parsing the arguements.
parser = argparse.ArgumentParser()
parser.add_argument('lsHostname', type=str, help='Root Server Host Name')
parser.add_argument('lsListenPort', type=int, help='Root Server Port Number')
args = parser.parse_args()

lsPORT = args.lsListenPort
hostname = args.lsHostname

def client():

    dataStore = []

    try:        
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client Socket has been created.")
    except socket.error as err:
        print("Socket Open Error: " + err)
        
    serverBinding = (hostname, lsPORT)
    clientSocket.connect(serverBinding)

    file = open("PROJI-HNS.txt", "r")
    failSwitch = True

    for line in file:
        originalLine = line
        line = line.lower()
        clientSocket.sendall(line.encode('utf-8'))
        print("Waiting 5 seconds")
        time.sleep(5) # Make the client wait for a message from the Root Server.
        print("5 minute wait is complete, check whether we received a response or not.")
        lsResponse = clientSocket.recv(1024).decode('utf-8')
        print("The response from the DNS, if any, is: " + lsResponse)

        if lsResponse == "": # if not lsResponse:
            dataStore.append(originalLine + " - Error:HOST NOT FOUND")
            continue
        
        dataStore.append(lsResponse)

    file.close()

    clientSocket.close()

    # At the end, write all the data from Data Store to the RESOLVED.txt.

    file = open("RESOLVED.txt", "w")
    counter = 0
    for entry in dataStore:
        lastIndex = len(dataStore) - 1
        if counter == lastIndex:
            file.write(entry)
        else:
            file.write(entry+'\n')

        counter += 1
    file.close()

    exit()

t1 = threading.Thread(name='client', target=client)
t1.start()
exit()