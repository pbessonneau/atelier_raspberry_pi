#!/usr/bin/python
import sys
import os
import datetime

from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

temp = sense.get_temperature()
print("Temperature: %s C" % temp)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

dateheure = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

fh = open("temp.csv", 'a')
fh.write("%s;%s;%s;%s\n" % (dateheure,temp,humidity,pressure))

