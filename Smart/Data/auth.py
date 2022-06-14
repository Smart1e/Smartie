import smartieJson as sj;import os;import sys;from time import sleep;from cryptography.fernet import Fernet

key = sj.read('key')
password = sj.read('password')
crypter = Fernet(key)

decrypt_pass = crypter.decrypt(password)



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
    if code['passUsed'] != 0:
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