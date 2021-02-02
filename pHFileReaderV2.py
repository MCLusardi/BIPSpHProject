#Python code for connecting Arduino to Python
#Source: That's Engineering 29/04/2020
#This code has been adapted from Chams123456 by MC Lusardi for BIPS at the University of Missouri
#The purpose is to read data from an Arduino Mega receiving data from two pH sensors 
#and save it to a CSV file. It must be run with the Arduino script 'arduino_mega_pH_2sensors.ino'
#This is the second version of this script. It has (or is going to be) altered to:
#   read one line from the given arduino and stop
#   read from multiple ports at the same time
#   accept parameters for filename and port name

import serial
import time
#import schedule


def main_func():
    print('Entered main_func()')
    
    #Establish connections with both arduinos
    arduino1 = serial.Serial('/dev/ttyACM1', 9600)
    print('Established serial connection to arduino1')
    arduino2 = serial.Serial('/dev/ttyACM0', 9600)
    print('Established serial connection to arduino2')
    
    #Create variables to hold and decode data from each arduino
    arduino_data1 = arduino1.readline()
    arduino_data2 = arduino2.readline()

    decoded_values1 = str(arduino_data1[0:len(arduino_data1)-2].decode("utf-8"))
    decoded_values2 = str(arduino_data2[0:len(arduino_data2)-2].decode("utf-8"))

    print('Collected readings from Arduino: {}, {}'.format(decoded_values1, decoded_values2))
    file.write(time.asctime(time.localtime(time.time())))
    file.write(',')
    file.write(decoded_values1 + ',' + decoded_values2)
    file.write('\n')
    file.close()

    arduino_data1 = 0
    arduino_data2 = 0
    arduino1.close()
    arduino2.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used

#print('Program started')`
file = open("newScriptTest.txt", "a")
file.write("date, s2, s1\n")
main_func()
file.close()
