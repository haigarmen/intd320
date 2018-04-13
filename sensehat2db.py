#!/usr/bin/python3

from sense_hat import SenseHat
import time
import MySQLdb as mdb
import os

sense = SenseHat()
sense.clear()

humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())


def getTemp():
    t= os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpuTemp = t.read()
    cpuTemp = cpuTemp.replace('temp=','')
    cpuTemp = cpuTemp.replace('\'C\n','')
    cpuTemp = float(cpuTemp)
    
    temp = sense.get_temperature()
    
    calcTemp = temp - ((cpuTemp -temp)/2)
    calcTemp = round(calcTemp)
    return calcTemp

while True:
    print(getTemp())
    time.sleep(2)
