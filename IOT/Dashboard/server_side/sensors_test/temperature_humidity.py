import Adafruit_DHT
import time

#comment and uncomment the lines below depending on your sensor
#sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT22
#sensor = Adafruit_DHT.AM2302

#DHT pin connects to GPIO 4
sensor_pin = 4

#create a variable to control the while loop
running = True

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)


        #sometimes you won't get a reading and
        #the results will be null
        #the next statement guarantees that
        #it only saves valid readings
        if humidity is not None and temperature is not None:

            #print temperature and humidity
            print('Temperature = ' + str(temperature) + 'Humidity = ' + str(humidity))
            time.sleep(1)

        else:
            print('Failed to get reading. Try again!')
            time.sleep(1)

    except KeyboardInterrupt:
        print ('Program stopped')
        running = False