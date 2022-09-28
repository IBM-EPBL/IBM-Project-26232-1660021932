from random import *
from time import *

loop = 1
while(loop):
    t = randint(0, 50) # temperature
    h = randint(0,100) # humidity
    print("Temperature(in celsius) -> ", t, "& Humidity : ", h)
    if t > 25 and h < 25:
        print("alarm & sprinkler ON")
        sleep(1)
        loop = 0
    else:
        print("alarm OFF")
        sleep(1)
