#!/usr/bin/env python
# LED with 560 Ohm resistor on Pin 10 to GND
# Tony Goodhew - 10 May 2013
from nanpy import Arduino
from nanpy import serial_manager
serial_manager.connect('/dev/ttyACM0')        # serial connection to Arduino
from time import sleep
import time
#import plotly.plotly as py
#import json
import time
import datetime
from drawnow import *
import matplotlib.pyplot as plt
#from bokeh import pyplot
#from bokeh import plotting
import mpld3

#with open('./config.json') as config_file:
    #plotly_user_config = json.load(config_file)

#py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

#url = py.plot([
    #{
        #'x': [], 'y': [], 'type': 'scatter',
        #'stream': {
            #'token': plotly_user_config['plotly_streaming_tokens'][0],
            #axpoints': 200
        #}
    #}], filename='aRi Analytics Demonstration')

#print "View your streaming graph here: ", url

LED =10                        # LED on Arduino Pin 10 (with PWM)
# for measuring temperature
analogPort = 0
powervoltage = 5.
tempC = []
Arduino.pinMode(LED, Arduino.OUTPUT)
#Arduino.pinMode(analogPort, Arduino.INPUT)

# function makeFig()

def makeFig():
	plt.ylim(20,80)
	plt.title('Temperature Streaming')
	plt.grid(True)
#	plt.ylable('Temp C')
	plt.plot(tempC, 'ro-',label='Degree C')
	plt.legend(loc='upper left')
#	pyplot.show_bokeh(plt.gcf(), filename="mpltest.html")
#	plotting.session().dumpjson(file="mpltest.json")
        mpld3.show()
#	plt.show()		
print"Starting"
print"5 blinks"
for i in range(0,2):
    Arduino.digitalWrite(LED, Arduino.HIGH)
    sleep(0.5)
    Arduino.digitalWrite(LED, Arduino.LOW)
    sleep(0.5)

print"Changing brightness of LED"
bright = 128                           # Mid brightness
Arduino.analogWrite(LED, bright)
Arduino.digitalWrite(LED,Arduino.HIGH)          # Turn on LED

for i in range(0,200):
    bright = bright + 8
    if (bright > 200):          # LED already full on at this point
        bright = 0          # Minimum power to LED
    Arduino.analogWrite(LED, bright)           # Change PWM setting/brightness
    sleep(0.05)

Arduino.digitalWrite(LED,Arduino.LOW)          # Turn off LED
print"Finished"
print "now showing the temperature...."
#stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
#stream.open()
cnt = 0

try:
    while True:
        sensorValue = Arduino.analogRead(analogPort)
        temperature = (sensorValue/1023.)*powervoltage*100
     #   f = open('temp.txt','a')
    #    f.write("room 1  " + str(datetime.datetime.now()) + "  " + str(temperature) + "\n")
        print "room 1 ", datetime.datetime.now() ,"  ",temperature
        # write the data to plotly
        #stream.write({'x': datetime.datetime.now(), 'y': temperature})
        tempC.append(temperature)
	drawnow(makeFig)
#	plt.plot(tempC)
#	mpld3.show()
	plt.pause(.00001)
	cnt=cnt+1
	print "cnt=   ", cnt
	if(cnt>50):
		tempC.pop(0)
#        sleep(0.25)
except KeyboardInterrupt:
    print "...cleaning up GPIO..."
    print time.time()
    print "GPIO has been cleaned up...."
    #f.close()
    
    
    

    

