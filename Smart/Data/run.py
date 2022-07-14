
from auth import authenticate
import sys
from SmartieWindows_modular import main

authed = authenticate()

if authed == 0:
    sys.exit()
    
elif authed == 1:
    print('Authenticated')
    while True:
        main()
        
else:
    print('Error')
    sys.exit()
    