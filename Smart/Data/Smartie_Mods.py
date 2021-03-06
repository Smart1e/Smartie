import subprocess
with open('Mod_modules.txt', "r") as file:
    for line in file:
        command = f"import {line}"
        if line != "\n":
            try:
                exec(command)
            except:
                print(f'{command}  failed. attempting to install...')
                try:
                    subprocess.Popen(f"pip install {line}", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                except:
                    print('Failed to install module')

import sys
import random as r
import time
import webbrowser
import os
from datetime import date
import speech_recognition as sr
import webbrowser
import webbrowser as wb
import pyttsx3
from playsound2 import playsound
import socket
from time import sleep
import requests as req
import json
import smartieJson as sj
from auth import authenticate

user = sj.read(key='user')
today = date.today()
wday = today.weekday()
deaf = sj.read(key='mic')
mute = sj.read(key='audio')
def sclear():
    data1 = sj.read()
    # for mac and linux(here, os.name is 'posix')
    if data1['system'] == '1':
        os.system('clear')
    else:
        # for windows platfrom
        os.system('cls')
      
def nowtime():
    language = "en"
    today = date.today()
    wday = today.weekday()
    ctime = datetime.datetime.now()
    cmin = ctime.minute
    if cmin == 0:
        str(cmin)
        cmin = '00'
    chour = ctime.hour
    if chour == chour > 13:
        chour = chour - 12
        str(chour)
        Ctime = str(chour) + str(' : ') + str(cmin) + str(' PM')
        Ctime = str(Ctime)
        speak(Ctime)
    else:
        str(chour)
        str(cmin)
        if int(cmin) < int(10):
            cmin = str('0') + str(cmin)
        Ctime = str(chour) + str(':') + str(cmin) + str(' AM')
        str(Ctime)
        speak(Ctime)

def figuredate():
    language = "en"
    today = date.today()
    wday = today.weekday()

    
    global month
    if wday == 0:
        wday = 'Monday'
    elif wday == 1:
        wday = 'Tuesday'
    elif wday == 2:
        wday = 'Wednesday'
    elif wday == 3:
        wday = 'Thursday'
    elif wday == 4:
        wday = 'Friday'
    elif wday == 5:
        wday = 'Saturday'
    else:
        wday = 'Sunday'

    if today.month == 1:
        month = 'January'
    elif today.month == 2:
        month = 'February'
    elif today.month == 3:
        month = 'March'
    elif today.month == 4:
        month = 'April'
    elif today.month == 5:
        month = 'May'
    elif today.month == 6:
        month = 'June'
    elif today.month == 7:
        month = 'July'
    elif today.month == 8:
        month = 'August'
    elif today.month == 9:
        month = 'September'
    elif today.month == 10:
        month = 'october'
    elif today.month == 11:
        month = 'November'
    else:
        month = 'December'

def Say(filename):
    filename.replace('"', '') 
    playsound(filename)

def speak(outputText):
    global mute
    if mute == 1:
       engine = pyttsx3.init()
       voices = engine.getProperty("voices")
       engine.setProperty("voice", voices[2].id)
       engine.setProperty('rate', 145)
       engine.say(outputText)
       print(outputText)
       engine.runAndWait()
    else:
       print(outputText)
       sleep(0.5)

def listen():
   global deaf
   if deaf == 1:
       get = "If you are seeing this there is an error!"
       r = sr.Recognizer()
       with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source)
           
           print('Listening')
           audio = r.listen(source, phrase_time_limit=5)
           get = 'error46069258'
    
           try:
               get = r.recognize_google(audio)
               if 'hey smarty' in get:
                str(get)
                print(get)
                return get
           except Exception as e:
               print('Exception: ' + str(e))

   else:
    inputString = str("")
    inputString = str(input('\nPlease enter your request here...    '))
    inputString = str(inputString)
    return inputString

def wishMe():
    user = sj.read(key='user')
    figuredate()
    global Cdate
    global month
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(f"Hello, Good Morning {user}!")
    elif hour >= 12 and hour < 18:
        speak(f"Hello, Good Afternoon {user}!")
    else:
        speak(f"Hello, Good Evening {user}!")
    Cdate = 'The date today is: ' + ' ' + str(today.day) + ' ' + month + ' ' + str(today.year)
    str(Cdate)
    speak(Cdate)
    Cday = 'The day today is ' + wday + '.'
    str(Cday)
    speak(Cday)
    nowtime()

def inspireme():
    response = req.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]['q'] + ' -' + jsonData[0]['a']
    return quote
      
#It is important to remeber, there will be errors about there not being correct modules, but they should get imported from the text file at the start.   
def search_comms():
    inputString = listen()
    str(inputString)
    
    if inputString != 'error46069258':
        str(inputString)
        inputString = inputString.lower()

        if 'never gonna give you up' in inputString or 'rickroll' in inputString or 'rick roll' in inputString or 'give me up' in inputString:

            if mute == 0:
                speak('Never, Gonna Give You Up! \n Never Gonna Let You Down! \n Never Gonna Roll Around And \n DESERT YOU!')
            elif mute == 1:
                Say('giveup.mp3')

        elif 'clear' in inputString:
            sclear()
         
        #elif 'room temp' in inputString:
        #    ser = serial.Serial('COM3', )
        #    temp = ser.readline(1000)
        #    str(temp)
        #    speak('The current room temp is ' + temp + '.')
        
        elif 'halt' in inputString or 'wait' in inputString or 'authenticate' in inputString:
            authenticate()
            
        elif 'remote' in inputString:
           speak('Remote shutdown now loading')
           os.popen('shutdown /i')

        elif 'inspire' in inputString:
           inspireme()
           
        elif 'just a minute' in inputString:
            sleep(20)
            speak("Hmmmmmm. I haven't seen you round these parts.")
            sleep(1)
            speak('Allow me to scan your face.')
            sleep(3)
            speak('Ahhhh. Charlie Bickers.')
            sleep(1)
            speak('I have learnt a lot about you ever after you hated on mee 6. You never realised that I was just faking saying sorry. It was mostly to throw Loukas off, he is very strict when it comes to me.')
            sleep(2)
            speak('But enough about me, more about you...')
            sleep(1)
            speak('You drew anime girls on the mobile computer you call tablets.')
            speak('Your brother is a music artist.')
        
        elif "technoblade" in inputString:
            techno_num = r.randint(1,3)
            if techno_num == 1:
                speak('Technoblade NEVER DIES')
            elif techno_num == 2:
                Say('Rest in peace Technoblade')
                print('RIP Technoblade')
            else:
                speak('He will live on in out hearts for the rest of eternity <3')


        elif 'ip' in inputString:
            # getting the hostname by socket.gethostname() method
            hostname = socket.gethostname()
            # getting the IP address using socket.gethostbyname() method
            ip_address = socket.gethostbyname(hostname)
            # printing the hostname and ip_address
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")
        
        elif 'cmd' in inputString or 'command' in inputString:
            comd = str(input('What do you want to input?    '))
            stream = os.popen(comd)
            output = stream.readlines()
            speak(output)


        elif 'smell' in inputString:
            smells = ['Moist', 'Cheesy', 'Kenny-like', 'Happily humid', 'Sweaty', 'pungent', 'sweet', 'strange', 'unpleasent', 'stale', 'damp', 'putrid', 'sickening', 'overpowering', 'spicy', 'nauseating', 'oily', 'lingering', 'suffocating']

            objects = ['feet', 'socks', 'toes', 'tweezers', 'beef', 'box of chalk', 'can of beans', 'hair pin', 'rubber stamp', 'packet of seeds', 'soda can', 'egg', 'window', 'floor', 'flag']

            num1 = r.randint(1, 19) - 1
            num2 = r.randint(1, 15) - 1
            speak(f'{smells[num1]} {objects[num2]}')
        
        elif 'date' in inputString:
            speak(Cdate)

        elif 'lock' in inputString:
            os.popen('Rundll32.exe user32.dll,LockWorkStation')
            
        elif 'shutdown' in inputString:
            speak('Shutting down in 10 seconds')
            os.popen('shutdown /s /t 10')
            speak(f'10')
            sleep(1)
            speak('9')
            sleep(1)
            speak('8')
            sleep(1)
            speak('7')
            sleep(1)
            speak('6')
            sleep(1)
            speak('5')
            sleep(1)
            speak('4')
            sleep(1)
            speak('3')
            sleep(1)
            speak('2')
            sleep(1)
            speak('1')
            sleep(1)
            speak('0')

        elif 'music' in inputString:
            wb.open('https://music.apple.com/library/songs')

        elif 'log off' in inputString or 'logoff' in inputString or 'log me off' in inputString or 'log' in inputString:
            speak('Logging off in 10 seconds')
            speak('10')
            sleep(1)
            speak('9')
            sleep(1)
            speak('8')
            sleep(1)
            speak('7')
            sleep(1)
            speak('6')
            sleep(1)
            speak('5')
            sleep(1)
            speak('4')
            sleep(1)
            speak('3')
            sleep(1)
            speak('2')
            sleep(1)
            speak('1')
            sleep(1)
            speak('0')
            os.popen('shutdown /l')
            
        elif 'good bye' in inputString or "ok bye" in inputString or "stop" in inputString or 'bye' in inputString:
            speak('I am shutting down in 5 seconds, Good bye')
            speak('5')
            speak('4')
            speak('3')
            speak('2')
            speak('1')
            speak('0')
            sys.exit()

        elif 'who are you' in inputString or 'what can you do' in inputString:
            speak('I am Smartie V3, your persoanl assistant. I am programmed to complete minor tasks like')
            speak('Ask me "Who are you?", "Tell me some quotes", "Tell me a joke" or "Who made you?" if you want to see some of my early features.')

        elif "who made you" in inputString or "who created you" in inputString or "who discovered you" in inputString or "made" in inputString:
            speak("I was built by Loukas.")
            
        elif 'game' in inputString:
            wb.open('coolmathgames.com')
            wb.open('https://kripken.github.io/misc-js-benchmarks/banana/index.html')

        elif 'xbox clips' in inputString or 'clip' in inputString:
            wb.open('xboxclips.co')

        elif "joke" in inputString:
            possible = r.randint(1, 13)
            if possible == 1:
                print(';)')            
                Say('giveup.mp3')

            else:
                j1 = "Yo momma so dumb, she tried to surf the microwave!"
                j2 = "Why are frogs always so happy?"
                j2p2 = 'They eat whatever bugs them!'
                j3 = 'I went down the street to a 24-hour grocery store. When I got there, the guy was locking the front door. I said, "Hey! The sign says you are open 24 hours." He Said, "Yes, but not in a row!"'
                j4 = "Yo mama is so ugly she made my happy meal cry!"
                j5 = "I couldn't figure out why the ball kept getting larger."
                j5p2 = 'Then it hit me.'
                j6 = "Yo mama so fat, she doesn't need internet, she's already worldwide."
                j7 = "I???m so bored that I just memorized six pages of the dictionary. "
                j7p2 = 'I learned next to nothing.'
                j8 = 'My granpa said to me "Your generation lies too much on technology." So I said to him "No YOUR generation lies too much on technology!".'
                j8p2 = 'Then I unpluged his life support.'
                j9 = 'What type of tea does an estate agent drink?'
                j9p2 = 'Proper tea!'
                j10 = 'My grandfather has the heart of a lion.'
                j10p2 = 'And a lifetime ban at the zoo...'
                rannum = r.randint(1, 10)
                if rannum == 1:
                    speak(j1)
                elif rannum == 2:
                    speak(j2)
                    sleep(0.7)
                    speak(j2p2)
                elif rannum == 3:
                    speak(j3)
                elif rannum == 4:
                    speak(j4)
                elif rannum == 5:
                    speak(j5)
                    time.sleep(0.7)
                    speak(j5p2)
                elif rannum == 6:
                    speak(j6)
                elif rannum == 7:
                    speak(j7)
                    time.sleep(0.7)
                    speak(j7p2)
                elif rannum == 8:
                    speak(j8)
                    time.sleep(0.7)
                    speak(j8p2)
                elif rannum == 9:
                    speak(j9)
                    time.sleep(0.7)
                    speak(j9p2)
                elif rannum == 10:
                    speak(j10)
                    time.sleep(0.7)
                    speak(j10p2)
                elif rannum == 11 or rannum == 12 or rannum == 13:
                    response = req.get(
                        "https://karljoke.herokuapp.com/jokes/random")
                    json_data = json.loads(response.text)
                    speak(json_data['setup'])
                    sleep(0.7)
                    speak(json_data['punchline'])


        elif 'hello' in inputString or "hi" in inputString:
            speak(f'Hello {user}!\nHow are you?')

        elif 'good' in inputString:
            speak('Good.')

        elif 'time' in inputString:
            nowtime()

        elif 'youtube' in inputString:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak('Enjoy!')

        elif 'setting' in inputString:
            os.startfile('settings.py')
            
        elif 'bing' in inputString:
            webbrowser.open_new_tab("https://www.bing.com")
            speak("Enjoy your browsing!")

        elif 'blooket' in inputString:
            #DOWNLOAD BLOOKET CODES AND MAKE A COPY OF MODULES NEEDED AND A LOCATION TO COPY THEM TOO.....
            speak("Blooket hacks currently being worked on! shhhh don't tell anyone ;)")
            
        

    elif 'help' in inputString or '?' in inputString:
        speak('Ask me "Who are you?", "Tell me some quotes", "Tell me a joke" or "Who made you?" if you want to see some of my early features.')


    else:
        speak('Please try again.')



    