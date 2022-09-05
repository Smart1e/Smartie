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

attempt = 0
result = 69

#The auth function
def attempt_auth():
    def authenticate(input):
        global attempt
        #password = sj.read('password')
        password = 'Password'
        #if code['passUsed'] != '0':
        if True:
            while attempt < 4:
                
                
                if input == password:
                    result = 1
                    root.destroy()
                    
                elif input != password and attempt == 3:
                    result = 0
                    incorect_pass_label.grid(row=2, column=0, columnspan=2)
                    

                elif input != password and attempt > 3:
                    result = 0
                    incorect_pass_label.grid(row=2, column=0, columnspan=2)
                    
                    
                else:
                    attempt=attempt+1
                    final_incorect_pass_label.grid(row=2, column=0, columnspan=2)
                    result = 2
                    
        else:
            return(2)
    
    def choose_return(num):
        global result
        result = num
        
        
    import tkinter as tk

    root = tk.Tk()

    enter_pass_label = tk.Label(root, text='Enter Passcode: ')
    enter_pass_box = tk.Entry(root, show='*')

    incorect_pass_label = tk.Label(root, text='Incorrect Passcode')
    final_incorect_pass_label = tk.Label(root, text='Please try again later...')
    correct_pass_label = tk.Label(root, text='Correct Passcode, press continue to continue.')

    enter_button = tk.Button(root, text='Enter', command=lambda: authenticate(enter_pass_box.get()))
    continue_button = tk.Button(root, text='Continue', command=lambda: root.destroy())

    enter_pass_label.grid(row=0, column=0, columnspan=2, pady=3)
    enter_pass_box.grid(row=0, column=2, columnspan=2, pady=3)
    
    enter_button.grid(row=5, column=0, columnspan=2, pady=3)

    root.mainloop()
    return result


attempt_auth()