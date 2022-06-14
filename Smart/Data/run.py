from tkinter.messagebox import NO
from auth import authenticate
import sys


authed = authenticate()

if authed == 0:
    sys.exit()
    
elif authed == 1:
    print('Authenticated')
    
else:
    print('Error')
    sys.exit()
    
from SmartieWindows import main

while True:
    main()