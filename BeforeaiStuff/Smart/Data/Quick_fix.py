
import subprocess
from awesome_progress_bar import ProgressBar
from time import sleep







def start_fix():
    bar = ProgressBar(total=30, prefix='Progress:', suffix='Complete',
                  bar_length=50, fill='X')
    with open("Mod_modules.txt", "r") as file:
        for line in file:
            try:
                _ = subprocess.Popen(f"pip install {line}", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            except:
                bar.stop()
                
        bar.iter()
    with open('Modules.txt', 'r') as file:
        for line in file:
            try:
                _ = subprocess.Popen(f"pip install {line}", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                
            except:
                bar.stop()
        bar.iter()
    bar.stop()
    print('Completed!')
    sleep(5)
