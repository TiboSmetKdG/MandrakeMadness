from machine import I2C
from machine import Pin
from SI7021 import SI7021
import time

relay = Pin('P2', mode=Pin.OUT)
i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)

while True:
    temperature = si7021.temperature()
    humidity = si7021.humidity()
    dew_point = si7021.dew_point()
    serial = si7021.serialnumber
    print(str(round(humidity,2)) + " %")
    print(str(round(temperature,2)) + " °C")

    if humidity <= 70:
        i = 0
        while (i < 15):
            relay.value(1)
            i += 1
            sleep(1)
    else:
        relay.value(0)
    time.sleep(1)
