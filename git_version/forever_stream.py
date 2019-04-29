import subprocess
from datetime import datetime

k = 0 
while True:
    subprocess.run("python3 stream.py", shell = True, stdout=subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    fail = datetime.now()
    k += 1
    print(str(k) + " failure at " + str(fail))