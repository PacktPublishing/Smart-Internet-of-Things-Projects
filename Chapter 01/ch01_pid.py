import matplotlib
matplotlib.use('Agg')

import PID
import Adafruit_DHT
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

sensor = Adafruit_DHT.DHT22

# DHT22 pin on Raspberry Pi
pin = 23

P = 1.4
I = 1
D = 0.001
pid = PID.PID(P, I, D)

pid.SetPoint = 0.0
pid.setSampleTime(0.25)  # a second

total_sampling = 100
sampling_i = 0
measurement = 0
feedback = 0

feedback_list = []
time_list = []
setpoint_list = []

print('PID controller is running..')
try:
    while 1:
        pid.update(feedback)
        output = pid.output

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:

            # ## testing
            # if 23 < sampling_i < 50:
            #     temperature = 27.46
            #
            # if 65 <= sampling_i < 75:
            #     temperature = 24.58
            #
            # if sampling_i >= 85:
            #     temperature = 19.26
            # ################

            if pid.SetPoint > 0:
                feedback += temperature + output

            print('i={0} desired.temp={1:0.1f}*C temp={2:0.1f}*C pid.out={3:0.1f} feedback={4:0.1f}'
                  .format(sampling_i, pid.SetPoint, temperature, output, feedback))
            if output > 0:
                print('turn on heater')
            elif output < 0:
                print('turn on cooler')

        if 20 < sampling_i < 60:
            pid.SetPoint = 28  # celsius

        if 60 <= sampling_i < 80:
            pid.SetPoint = 25  # celsius

        if sampling_i >= 80:
            pid.SetPoint = 20  # celsius

        time.sleep(0.5)
        sampling_i += 1

        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        time_list.append(sampling_i)

        if sampling_i >= total_sampling:
            break

except KeyboardInterrupt:
    print("exit")


print("pid controller done.")
print("generating a report...")
time_sm = np.array(time_list)
time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
feedback_smooth = spline(time_list, feedback_list, time_smooth)

fig1 = plt.gcf()
fig1.subplots_adjust(bottom=0.15, left=0.1)

plt.plot(time_smooth, feedback_smooth, color='red')
plt.plot(time_list, setpoint_list, color='blue')
plt.xlim((0, total_sampling))
plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))
plt.xlabel('time (s)')
plt.ylabel('PID (PV)')
plt.title('Temperature PID Controller')


plt.grid(True)
fig1.savefig('pid_temperature.png', dpi=100)
print("finish")

