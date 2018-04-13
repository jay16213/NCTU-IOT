import time, DAN, requests, random

ServerIP = '140.113.199.204' #Change to your IoTtalk IP or None for autoSearching
Reg_addr=None #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control','OneParameter','ThreeParameter']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

switch = 0

while True:
    # try:
    #Pull data from a device feature called "Dummy_Control"
    value1=DAN.pull('Dummy_Control')
    if value1 != None:
            #print(type(value1))
            #print(len(value1))
        if value1[0] != None:
            # print(value1[0][0])
            # print(value1[0][1])
            if value1[0][0] > 0:
                switch = 1
            else:
                switch = 0

        if switch == 1:
            print("x: {}, y: {}, z: {}".format(value1[0][1][0], value1[0][1][1], value1[0][1][2]))

    # except Exception as e:
    #     print(e)
    #     DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
