
from auth import attempt_auth
import sys
from SmartieWindows_modular import main
import smartieJson as sj

if sj.read('passUsed') == '1':
    authed = attempt_auth()

    if authed == 0:
        sys.exit()
        
    elif authed == 1:
        print('Authenticated')
        while True:
            main()
            
    elif authed == 2:
        while True:
            main()
            
    else:
        print('Error')
        sys.exit()
        
else:
    while True:
        main()
    