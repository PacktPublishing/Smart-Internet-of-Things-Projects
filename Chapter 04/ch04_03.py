import serial

serial_hc06 = '/dev/cu.HC-06-DevB'
counter = 0

print('open ', serial_hc06)
hc06 = serial.Serial(serial_hc06, 9600)

while True:
    try:
        # python 3.x
        #c = input('>> ')

        # python 2.7.x
        c = raw_input('>> ')

        if c == 'q':
            break

        hc06.write(c)

    except (KeyboardInterrupt, SystemExit):
        hc06.close()
        raise

print('Exit')
