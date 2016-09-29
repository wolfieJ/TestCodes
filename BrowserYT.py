import time
import datetime
import urllib
import webbrowser
import random
import os
from sys import argv


filename = argv
print("Source Code Path:%r" % filename)
alarm = input('Set alarm at HH:MM:SS- ' )
with open("YTlinks.txt") as f:
        content = f.readlines()
print (content)

random_video = random.choice(content)
print ('\n',random_video)



Time = time.strftime("%H:%M:%S")


while Time != alarm:
    Time = time.strftime("%H:%M:%S")

    print('Current time is'+' '+Time)
    time.sleep(1)

if Time == alarm:
    print('It''s YouTube time!')
    webbrowser.open(random_video)






