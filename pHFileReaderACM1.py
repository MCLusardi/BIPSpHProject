#Python code for connecting Arduino to Python
#Source: That's Engineering 29/04/2020
#This code has been adapted from Chams123456 by MC Lusardi for BIPS at the University of Missouri
#The purpose is to read data from an Arduino Mega receiving data from two pH sensors 
#and save it to a CSV file. It must be run with the Arduino script 'arduino_mega_pH_2sensors.ino'

import serial
import time
#import schedule


def main_func():
    #print('Entered main_func()')
    #May have to change port depending on the computer
    arduino = serial.Serial('/dev/ttyACM1', 9600)
    #print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    string_value = decoded_values

    #print(f'Collected readings from Arduino: {string_value}')
    file.write(time.asctime(time.localtime(time.time())))
    file.write(',')
    file.write(string_value)
    file.write('\n')
    file.close()

    arduino_data = 0
    arduino.close()
    #print('Connection closed')
    #print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
#list_values = []
#list_in_floats = []

#print('Program started')
file = open("Day1_3pHACM1.txt", "a")
file.write("date, s2, s1\n")
file.close()
#file = open("Test3PHOutputACM0.txt", "a")
# Setting up the Arduino
#schedule.every(10).seconds.do(main_func)

while True:
    file = open("Day1_3pHACM1.txt", "a")
    main_func()
    #schedule.run_pending()
    time.sleep(10)
