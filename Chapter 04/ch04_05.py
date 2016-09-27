import serial
import sys

serial_hc06 = '/dev/cu.HC-06-DevB'
counter = 0

print('open ', serial_hc06)
hc06 = serial.Serial(serial_hc06, 9600)
print('read data from gps')
while True:
    try:
        c = hc06.read(1)
        if c != '':
            sys.stdout.write(c)
            sys.stdout.flush()

    except (KeyboardInterrupt, SystemExit):
        hc06.close()
        raise

print('Exit')
