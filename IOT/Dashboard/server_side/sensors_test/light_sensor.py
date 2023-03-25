import time
from smbus import SMBus
smbus = SMBus(1)

smbus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
smbus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
time.sleep(0.5)

while True:
    data = smbus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
    data1 = smbus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
    L = ch0-ch1

    print(L)
    time.sleep(1)