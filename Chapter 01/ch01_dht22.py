import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22

# DHT22 pin on Raspberry Pi
pin = 23


try:
    while 1:
        print("reading DHT22...")
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

        time.sleep(2)

except KeyboardInterrupt:
    print("exit")


print("done")

