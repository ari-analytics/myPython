import serial
ser = serial.Serial('/dev/ttyACM0',9600)
dataFile = 'data.txt'
f = open(dataFile,'a')

#ser.write('3')
try:
	while 1:
		temperature = ser.readline()
		f.write(temperature)

except KeyboardInterrupt:
	f.close()


