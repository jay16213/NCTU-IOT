import random

from dan import NoData

### The register server host, you can use IP or Domain.
host = '140.113.199.198'

### [OPTIONAL] The register port, default = 9992
# port = 9992

### [OPTIONAL] If not given or None, server will auto-generate.
# device_name = 'Dummy_Test'

### [OPTIONAL] If not given or None, DAN will register using a random UUID.
### Or you can use following code to use MAC address for device_addr.
# from uuid import getnode
# device_addr = "{:012X}".format(getnode())
#device_addr = "aa8e5b58-8a9b-419b-b8d5-72624d61108d"

### [OPTIONAL] If not given or None, this device will be used by anyone.
username = '0416213'

### The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'DM_0416213'

### The input/output device features, please check IoTtalk document.
idf_list = ['Dummy_Sensor']
odf_list = ['odf_0416213']

### Set the push interval, default = 1 (sec)
### Or you can set to 0, and control in your feature input function.
push_interval = 10  # global interval
interval = {
    'Dummy_Sensor': 3,  # assign feature interval
}

last_state = 0
state = 0

def register_callback():
    print('register successfully')

def Dummy_Sensor():
    return random.randint(0, 100)
    # return NoData

def Dummy_Control(data):  # data is a list
    print(data[0])

def odf_0416213(data):
    print(data[0])

    if data != None:
        #print(value[0])
        if data[0] >= 0:
            # last_state = state
            state = 1
        else:
            last_state = state
            state = 0

        if last_state != state:
            if state == 1:
                print("smart phone is up")
            else:
                print("smart phone is down")
