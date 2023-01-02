
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

text = input("Enter text:  ")
print('Waiting 3 Seconds')
sleep(3)
for char in text:
    keyboard.press(char)
    keyboard.release(char)
