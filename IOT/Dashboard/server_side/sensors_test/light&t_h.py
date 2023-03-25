import Adafruit_DHT
import time
from smbus import SMBus
import csv

smbus = SMBus(1)

smbus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
smbus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
time.sleep(0.5)

sensor = Adafruit_DHT.DHT22
sensor_pin = 4

def csvFileWriter(msg):
    with open("light_tem_hum.csv","a") as csvw:
        dataWriter = csv.writer(csvw)
        dataWriter.writerow(msg)
    csvw.close()
    
while True:
    data = smbus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
    data1 = smbus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
    L = ch0-ch1
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    values = [temperature ,humidity,L]
    humidity_str = format(humidity,".2f")
    temperature_str = format(temperature,".2f")
    print("temprature is :" +temperature_str+" humidity is :" +humidity_str+" light intensity is:"+str(L))
    csvFileWriter(values)
    time.sleep(1)
    
