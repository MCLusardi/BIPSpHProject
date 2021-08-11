#Python code for connecting three Arduinos or DFRduinos to a RasPi
#Source: That's Engineering 29/04/2020
#This code has been adapted from Chams123456 by MC Lusardi for BIPS at the University of Missouri
#The purpose is to read data from three Arduino Megas or DFRduinos receiving data from any number of sensors 
#and save it to a CSV file.

#To run you will need to edit this code
#first enter the command ls/dev/tty* in the terminal to find the list of active ports
#you will need to find which port numbers the arduinos are connected to as they may change each time you unplug and replug them into the RasPi
#You can see which port number they are by repeatedly running the command ls/dev/tty* and unplugging and replugging the arduino.
#When its port is in use, it will appear in the list of ports. When unplugged, the port it was using will no longer be listed
#There are a lot of ports that will be listed, but the ones you need will all begin with /dev/ttyACM or /dev/ttyUSB
#Once you know the port number for each arduino or DFRduino, you need to know the baud rate.
#   Arduino = 9600      DFRduino = 115200
#Once you know the port number and baudrate, you enter them into the serial functions in lines 27, 29, 31
# Example:   arduino1 = serial.Serial('port name', baud rate)

import serial
import time
import sys
import os.path 

def main_func():
    print('Entered main_func()')

    #Edit these lines
    arduino1 = serial.Serial('/dev/ttyACM1', 9600)
    print('Established serial connection to arduino1')
    arduino2 = serial.Serial('/dev/ttyACM0', 9600)
    print('Established serial connection to arduino2')
    arduino3 = serial.Serial('/dev/ttyACM2', 9600)
    print('Established serial connection to arduino3')

    #Create variables to hold and decode data from each arduino
    arduino_data1 = arduino1.readline()
    arduino_data2 = arduino2.readline()
    arduino_data3 = arduino3.readline()

    decoded_values1 = str(arduino_data1[0:len(arduino_data1)-2].decode("utf-8"))
    decoded_values2 = str(arduino_data2[0:len(arduino_data2)-2].decode("utf-8"))
    decoded_values3 = str(arduino_data3[0:len(arduino_data3)-2].decode("utf-8"))   

    print('Collected readings from Arduino: {}, {}, {}'.format(decoded_values1, decoded_values2, decoded_values3))
    file.write(time.asctime(time.localtime(time.time())))
    file.write(',')
    file.write(decoded_values1 + ',' + decoded_values2 + ',' + decoded_values3)
    file.write('\n')
    file.close()

    arduino_data1 = 0
    arduino_data2 = 0
    arduino_data3 = 0

    arduino1.close()
    arduino2.close()
    arduino3.close()

    #print('Connection closed')
    #print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------

#print('Program started')`
if(not os.path.isfile(sys.argv[1])):
    file = open(sys.argv[1], "a")
    file.write("date " + sys.argv[2] + "\n")
    file.close()
i=0
print(int(sys.argv[3]))
while(i < int(sys.argv[3])):
    time.sleep(300) #time between readings, should be 300 for 5 min readings
    print(i)
    file = open(sys.argv[1], "a")
    main_func()
    file.close()
    i += 1
