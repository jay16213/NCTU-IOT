import time, DAN, requests, random

ServerIP = '140.113.199.204' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='0416213' #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='0416213'
DAN.profile['df_list']=['0416213_DF']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

last_state = 0
state = 0

while True:
    try:
        # Pull data from a device feature called "Dummy_Control"
        value=DAN.pull('0416213_DF')
        if value != None:
            #print(value[0])
            if value[0] >= 0:
                last_state = state
                state = 1
            else:
                last_state = state
                state = 0

            if last_state != state:
                if state == 1:
                    print("smart phone is up")
                else:
                    print("smart phone is down")
            # if switch == 1:
            #     print("x: {}, y: {}, z: {}".format(value1[0][1][0], value1[0][1][1], value1[0][1][2]))

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
