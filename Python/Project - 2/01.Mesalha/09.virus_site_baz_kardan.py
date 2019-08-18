#NABEGHEHA.COM

import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com' , 'nabegheha.com'])
    webbrowser.open(sites)
    seconds = random.randrange(5,20)
    time.sleep(seconds)