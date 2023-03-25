import socket
import threading
import csv

PORT = 5055
IP = "192.168.1.9"
ADDR = (IP,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(client,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:       
        message = (client.recv(1024)).decode()
        if (message !=""):
            val = message.split(",")
            if (addr[0] =="192.168.1.4"):
                writeCsv1(val)
                print(f"{addr[0]}:{val}")
            elif (addr[0] == '192.168.1.3'):
                writeCsv2(val)
                print(f"{addr[0]}:{val}")
            elif (addr[0] == ''):
                writeCsv2(val)
                print(f"{addr[0]}:{val}")
            elif (addr[0] == ''):
                writeCsv2(val)
                print(f"{addr[0]}:{val}")

def start():
    server.listen()
    while True:
        client,addr = server.accept()
        print(client.getsockname())
        thread = threading.Thread(target=handle_client,args=(client,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")




def writeCsv1(msg):
    with open("data1.csv","a") as csvf1:
        dataWriter = csv.writer(csvf1)
        dataWriter.writerow(msg)
        csvf1.flush()
    csvf1.close()

def writeCsv2(msg):
    with open("data2.csv","a") as csvf2:
        dataWriter = csv.writer(csvf2)
        dataWriter.writerow(msg)
        csvf2.flush()
    csvf2.close()

def writeCsv3(msg):
    with open("data3.csv","a") as csvf3:
        dataWriter = csv.writer(csvf3)
        dataWriter.writerow(msg)
        csvf3.flush()
    csvf3.close()

def writeCsv4(msg):
    with open("data4.csv","a") as csvf4:
        dataWriter = csv.writer(csvf4)
        dataWriter.writerow(msg)
        csvf4.flush()
    csvf4.close()

print("Server is starting ....")
start() 