'''
import smartieJson as sj;import os;import sys;from time import sleep;from cryptography.fernet import Fernet

#Finding data from .json settings file
key = sj.read('key')
password = sj.read('password')

#encoding the string to bytes 

import chardet




key = str(key)
key = key.replace("b'", '')
key = key.replace("'", '')
#print('1', key)
#the_encoding = chardet.detect(key)['encoding']
#key_final = key.encode('utf-8')
key_final = bytes(key, 'ascii')
#key_final = bytes(key, 'PKCS7')
the_encoding = chardet.detect(key_final)['encoding']
#print(the_encoding)
#print(type(key_final))
#print(type(key))
#print((str(key_final)))


the_encoding = chardet.detect(key_final)['encoding']
print(the_encoding)


crypter = Fernet(key_final)

decrypt_pass = crypter.decrypt(password)
"""
def str2bytes(string):
    return 
    #Turns the string inputted into the function and turns it into a utf-8 encoded bytes format
    """

'''
import os
from time import sleep
import smartieJson as sj
# The screen clear function
def sclear():
   data1 = sj.read()
   # for mac and linux(here, os.name is 'posix')
   if data1['system'] == '1':
      os.system('clear')
   else:
      # for windows platfrom
      os.system('cls')

#The auth function
def authenticate():
    attempt = 0
    code = sj.read()
    password = sj.read('password')
    if code['passUsed'] != '0':
        while attempt < 4:
            
            pasin = str(input('Passcode?   '))
            if pasin == password:
                sclear()
                return(1)
                break
                
            elif pasin != password and attempt == 3:
                print('Final Incorrect')
                sleep(4)
                return(0)
                

            elif pasin != password and attempt > 3:
                print('Final Incorrect')
                sleep(4)
                return(0)
                
            else:
                print('Incorrect')
                attempt=attempt+1
    else:
        return(2)