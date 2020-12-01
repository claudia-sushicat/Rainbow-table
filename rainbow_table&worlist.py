# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:17:36 2020

@author: convi
"""
#raibow table
import hashlib
import json
from urllib import request

url = "https://raw.githubusercontent.com/umabatatahacker/Rainbow-table/main/data.json"
response = request.urlopen(url)
read = json.loads(response.read())

def list_password():
    global read
    password_list = []
    data_password = read["data"]
    for data in data_password:
        password_list.append(data["password"])
    return password_list


def password_with_hash():
   dictionary = {}
   for i in list_password():
       print(i,hashlib.sha256(i.encode()).hexdigest())
       dictionary[hashlib.sha256(i.encode()).hexdigest()]=i
   return dictionary
   

def decrypt(attempt_hash):
    dictionary = password_with_hash()
    if attempt_hash in dictionary:
        return dictionary[attempt_hash]
    else:
        return ('password not found')
    
    