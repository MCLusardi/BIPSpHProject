"""
	1/26/2021 - MC Lusardi
	This code is meant to read and send data from the Arduino Mega 2560 which is connected to the Atlas Scientific pH
    sensor. This program should be able to send commands to the arduino to control the sensor as well as receive pH
	data from the sensor every minute and print this data to a csv file. 
"""

#python reading test script

import serial
import time #for sleep and time
import re #regular expression operators

serialString = ""   #will hold input data
val = '0.00'
list = []
file = open("Trial2pHoutputACM0.txt", "w") #opening file for writing, will create if it doesn't exsit
if(file == None):
    print("File could not be opened\n")
else:
    file.write("pH, DateTime");
serialNumber = ""

#Opens a serial port for listening and stores it in variable serialPort
#serialPort will be how we manipulate serial methods
serialPort = serial.Serial("/dev/ttyACM0", baudrate = 9600)
print("Hello there")
print(serialPort.name)
#serialPort.write(b"C,5") #tell arduino to send data every 5 seconds
print("Sent message to serialPort")
serialPort.flush()

while(1):
    
    #Wait until there is data waiting in serial buffer
    if(serialPort.in_waiting > 0):
        
        #Read data out of the buffer until carriage return / newline
        serialString = serialPort.readline()
        serialPort.flush()

        serialStringAscii = serialString.decode('Ascii')
        if (serialStringAscii == "*ER\r"):
            print("string was equal to *ER")
            continue
        #Print the contents of serial data
        #print("Raw Data in serialPort")
        #print(serialStringAscii)
        
        #decoding into ascii for testing splitting
        
        
        
        #reg exp to pull out the value from the sensor to write to file
        serialNumber = (re.search(r'\d+\.\d+', serialString.decode('utf-8')))
        if serialNumber != None:
            #print("pH number")
            print(serialNumber.group())
            print(time.asctime(time.localtime(time.time())))
            file.write(str(serialNumber.group()))
            file.write(',') # so to split string by ':' when parsing for graphs
            file.write(time.asctime(time.localtime(time.time())))
            file.write('\n')

        
        #writing to TestOutput.txt file to store
        #format as %f %DATE_RECORDED
        

        #sleep(1) #for testing   
        
        #Tell we recieved data, commented out of example
        serialPort.write(b"Thank you for sending data \r\n")
        #the b in front of string indicates to send bytes!