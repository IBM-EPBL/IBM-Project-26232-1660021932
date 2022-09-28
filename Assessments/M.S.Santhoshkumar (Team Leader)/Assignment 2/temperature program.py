from random import *
from time import *

exit = True
while(exit):
    temperature = randint(-10, 50)
    humidity = randint(0,100)
    print("Temperature : " + str(temperature)  + "°C, Humidity : " + str(humidity) + "% ->", end=" ")

    
    if temperature > 30 and humidity < 20:
        print("Alarm and Water sprinkler goes ON")
        sleep(1)
        exit = False
    else:
        print("Alarm OFF")
        sleep(1)
