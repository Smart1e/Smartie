try:
    import tkinter as tk
    
except:
    import os
    modin1 = os.popen('pip install tkinter')
    if "'pip' is not recognized as an internal or external command" in str(modin1.read()):
        print('')