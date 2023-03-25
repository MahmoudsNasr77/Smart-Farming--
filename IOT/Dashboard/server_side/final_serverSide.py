import socket
import threading
import csv
import Adafruit_DHT
import datetime
import time
from smbus import SMBus

#server ip
SERVERIP = "192.168.1.7"

#ports
PORT1 =6000
PORT2 =6001
PORT3 =6002
PORT4 =6003

#light sensor info
smbus = SMBus(1)
smbus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
smbus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
time.sleep(0.5)

#temperature and humidity sensor info
sensor = Adafruit_DHT.DHT22
sensor_pin = 4

#get temperature , humidity and light readings
def read_temp_hum_light():
    #get light intensity
    data = smbus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
    data1 = smbus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
    light = ch0-ch1

    #get temperature and humidity
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    
    humidity_str = format(humidity,".2f")
    temperature_str = format(temperature,".2f")
    light_str = format(light,".2f")
    
    values = [temperature_str ,humidity_str,light_str]
    return values

#handel the server and get clients data then write it to a csv file
def handelSever(PORT):
    print("hell0")

    fileName = f"PORT{PORT}.csv"

    server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    info = (SERVERIP,PORT)
    server.bind(info)
    server.listen()

    while True:
        conn,addr = server.accept()      
        try:
            #receive clients data
            received_data = (conn.recv(1024).decode()).split(",")
		
		    #get current date and time
            ct = time.ctime()
            current_time = ct[11:20]
            current_date = ct[:10]+ct[19:]

            if not received_data:
                conn.close()
            else:  
                with open(fileName,"a") as csvf1:
                    csvWriter = csv.writer(csvf1)

			        #add date and time to the data
                    received_data.insert(0,current_time)
                    received_data.insert(1,current_date)                    
                    received_data.extend(read_temp_hum_light())
                    
		            #write received data to csv file
                    csvWriter.writerow(received_data)
                    print(received_data)

                conn.close()
        except:
            conn.close()

#start thread for each server
def start(): 
    thread1 = threading.Thread(target=handelSever,args=(PORT1,))
    thread2 = threading.Thread(target=handelSever,args=(PORT2,))
    thread3 = threading.Thread(target=handelSever,args=(PORT3,))
    thread4 = threading.Thread(target=handelSever,args=(PORT4,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
start()
