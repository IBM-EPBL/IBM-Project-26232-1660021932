import random
import time

while(1):
    t = random.randint(0, 50) 
    h = random.randint(0,100) 

    print("Temperature(in celsius) : ", t, end = " ")
    print("& Humidity : ", h)
    
    if t > 25 and h < 10:
        print("alarm ON")
        time.sleep(1)
        break
    else:
        print("alarm OFF")
        time.sleep(1)
