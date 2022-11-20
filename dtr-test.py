''' This program is for testing the DTR on the serial port.
    It is a simple program that will send a string to the serial port
    and then wait for a response.  The response is then printed to the
    screen. The program will then wait for a keypress before exiting.
    This program is designed to be run from the command line.
'''

import serial # Import the serial library
import serial.tools.list_ports
import time # Import the time library
import sys # Import the sys library
import inquirer # Import the inquirer library

# list of serial ports and select the one you want to use
ports = serial.tools.list_ports.comports()
port_list = []
port_desc = []
for port in ports:
    port_list.append(port.device)
    port_desc.append(port.description)

# select the serial port to use
questions = [ inquirer.List('port', message="Select the serial port to use", choices=port_list), ]
answers = inquirer.prompt(questions)
port = answers['port']

# Open the serial port
ser = serial.Serial(port, 9600, timeout=1)

# start DTR toggle 10 times
for i in range(10):
    # set the DTR line to 0
    ser.setDTR(0)
    print("DTR Line is set to 0")

    # Wait for the DTR line to settle
    time.sleep(0.5)

    # set the DTR line to 1
    ser.setDTR(1)
    print("DTR Line is set to 1")

    # Wait for the DTR line to settle
    time.sleep(0.5)

# Close the serial port
ser.close()

# exit the program
sys.exit()
