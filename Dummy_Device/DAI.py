import time, DAN, requests, random

ServerIP = '140.113.199.206' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='0416213' #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

last_state = 0
state = 0

before = 0
after = 0
cnt = 0
total = 0

while True:
    try:
        before = time.time()
        DAN.push('Dummy_Sensor', [9.8])
        value=DAN.pull('Dummy_Control')
        if value != None:
            after = time.time()
            cnt += 1
            if cnt == 10:
                print("avg: {}".format(total / 10))
            elif cnt < 10:
                print("time: {}".format(after - before))
                total += (after - before)

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
