#Python code for connecting Arduino to Python
#Source: That's Engineering 29/04/2020
#This code has been adapted from Chams123456 by MC Lusardi for BIPS at the University of Missouri
#The purpose is to read data from an Arduino Uno receiving data from two DFRobot  pH sensors 
#and save it to a CSV file. It must be run with the Arduino script '
#This is the second version of this script. It has (or is going to be) altered to:
#   read one line from the given arduino and stop
#   read from multiple ports at the same time
#   accept parameters for filename and port name

import serial
import time
import sys
import os.path 

def main_func():
    print('Entered main_func()')
    
    #Establish connections with both arduinos
    arduino1 = serial.Serial('/dev/ttyACM1', 9600)
    print('Established serial connection to arduino1')
    arduino0 = serial.Serial('/dev/ttyACM0', 9600)
    print('Established serial connection to arduino2')
    
    #Create variables to hold and decode data from each arduino
    arduino_data1 = arduino1.readline()
    arduino_data0 = arduino0.readline()

    decoded_values1 = str(arduino_data1[0:len(arduino_data1)-2].decode("utf-8"))
    decoded_values0 = str(arduino_data0[0:len(arduino_data0)-2].decode("utf-8"))

    print('Collected readings from Arduino: {}, {}'.format(decoded_values1, decoded_values0))
    #print('Collected readings from Arduino: {}'.format(decoded_values0))
    file.write(time.asctime(time.localtime(time.time())))
    file.write(',')
    file.write(decoded_values1 + ',' + decoded_values0)
    #file.write(decoded_values0)
    file.write('\n')
    file.close()

    arduino_data1 = 0
    arduino_data0 = 0
    arduino1.close()
    arduino0.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
# Make time a parameter, this will determine how many readings to make, or maybe infinite loop?
#print('Program started')`
if(not os.path.isfile(sys.argv[1])):
    file = open(sys.argv[1], "a")
    file.write("date,ACM1,ACM0\n")
    file.close()
i=0
print(int(sys.argv[2]))
while(i < int(sys.argv[2])):
    time.sleep(300) #time between readings
    print(i)
    file = open(sys.argv[1], "a")
    main_func()
    file.close()
    i += 1
