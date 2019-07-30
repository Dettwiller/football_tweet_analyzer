import subprocess
from datetime import datetime
import time

k = 0 
while True:
    subprocess.run("python3 analysis.py", shell = True, stderr = subprocess.DEVNULL)
    fail = datetime.now()
    k += 1
    print(str(k) + " failure at " + str(fail))
    time.sleep(30)