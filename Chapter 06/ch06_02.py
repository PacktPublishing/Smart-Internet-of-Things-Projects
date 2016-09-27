#!/usr/bin/env python

import random
import time
import sys
import iothub_client
from iothub_client import *


# messageTimeout - the maximum time in milliseconds until a message times out.
message_timeout = 10000

receive_context = 0
avg_temperature = 0
avg_humidity = 0
message_count = 3
received_count = 0

# global counters
receive_callbacks = 0
send_callbacks = 0

# MQTT as transport protocol
protocol = IoTHubTransportProvider.MQTT

# String containing Hostname, Device Id & Device Key in the format:
# "HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>"
connection_string = "[device connection string]"

msg_txt = "{\"deviceId\": \"<device_id>\",\"temperature\": %.2f,\"humidity\": %.2f}"

# some embedded platforms need certificate information
def set_certificates(iotHubClient):
    from iothub_client_cert import certificates
    try:
        iotHubClient.set_option("TrustedCerts", certificates)
        print("set_option TrustedCerts successful")
    except IoTHubClientError as e:
        print("set_option TrustedCerts failed (%s)" % e)


def receive_message_callback(message, counter):
    global receive_callbacks
    buffer = message.get_bytearray()
    size = len(buffer)
    print("Received Message [%d]:" % counter)
    print("    Data: <<<%s>>> & Size=%d" % (buffer[:size].decode('utf-8'), size))
    map_properties = message.properties()
    key_value_pair = map_properties.get_internals()
    print("    Properties: %s" % key_value_pair)
    counter += 1
    receive_callbacks += 1
    print("    Total calls received: %d" % receive_callbacks)
    return IoTHubMessageDispositionResult.ACCEPTED


def send_confirmation_callback(message, result, user_context):
    global send_callbacks
    print(
        "Confirmation[%d] received for message with result = %s" %
        (user_context, result))
    map_properties = message.properties()
    print("    message_id: %s" % message.message_id)
    print("    correlation_id: %s" % message.correlation_id)
    key_value_pair = map_properties.get_internals()
    print("    Properties: %s" % key_value_pair)
    send_callbacks += 1
    print("    Total calls confirmed: %d" % send_callbacks)


def iothub_client_init():
    # prepare iothub client
    iotHubClient = IoTHubClient(connection_string, protocol)
    # set the time until a message times out
    iotHubClient.set_option("messageTimeout", message_timeout)

    if iotHubClient.protocol == IoTHubTransportProvider.MQTT:
        iotHubClient.set_option("logtrace", 0)
    iotHubClient.set_message_callback(
        receive_message_callback, receive_context)
    return iotHubClient


def iothub_client_sample_run():

    try:

        iotHubClient = iothub_client_init()

        while True:
            # send a few messages every minute
            print("IoTHubClient sending %d messages" % message_count)

            for i in range(0, message_count):
                msg_txt_formatted = msg_txt % ((random.random() * 4 + 10), (random.random() * 4 + 60))
                # messages can be encoded as string or bytearray
                if (i & 1) == 1:
                    message = IoTHubMessage(bytearray(msg_txt_formatted, 'utf8'))
                else:
                    message = IoTHubMessage(msg_txt_formatted)
                # optional: assign ids
                message.message_id = "message_%d" % i
                message.correlation_id = "correlation_%d" % i
                # optional: assign properties
                prop_map = message.properties()
                prop_text = "PropMsg_%d" % i
                prop_map.add("Property", prop_text)
                iotHubClient.send_event_async(message, send_confirmation_callback, i)
                print(
                    "IoTHubClient.send_event_async accepted message [%d]"
                    " for transmission to IoT Hub." %
                    i)

            # Wait for Commands or exit
            print("IoTHubClient waiting for commands, press Ctrl-C to exit")

            n = 0
            while n < 6:
                status = iotHubClient.get_send_status()
                print("Send status: %s" % status)
                time.sleep(10)
                n += 1

    except IoTHubError as e:
        print("Unexpected error %s from IoTHub" % e)
        return
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")


if __name__ == '__main__':
    print('Demo Azure IoT Hub')
    iothub_client_sample_run()
