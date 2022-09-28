from random import *
from time import *

while(1):
    t = randint(0, 50) # temperature
    h = randint(0,100) # humidity

    print("Temperature -> ", t,"°C & Humidity : ", h, "%")
    
    if t > 30 and h < 10:
        print("alarm & sprinkler ON")
        sleep(1)
        break
    else:
        print("alarm OFF")
        sleep(1)
