#!/bin/python3

import requests

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSd63z5rAVie4clZ-PttFpHwCUJuhBeU6cCIbgsPGiZqbOz19g/formResponse'

form_data = ['entry.839337160' : 'this is a test']

r = requests.post(url, data=form_data)
