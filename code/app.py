#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module is application for the module for generic class to handle uart of a given intance. It makes a conenction to transmit data and recieve data. The setup of the uart are baudrate, start bits/no start bits, length of data bits and stop bits/no stop bits."
__file__ = "uart.py"
__class__ ="Uart"
__dependencies__ = ["DisplayMsg"]
#--------------------------------------------------------------------
#Version
#--------------------------------------------------------------------
__version_stage__ = "Pre_alpha"
__version_number__ = "0.1"
__version_date__ = "20140917"
__version_risk__ = "This current version is in Pre-alpha version, which meaning that the program can crash or perform other unrespected behavoiurs."
__version_modification__ = "The development project has just been created."
__version_next_update__ = "Implementation of connection."
#--------------------------------------------------------------------
#Hardware
#--------------------------------------------------------------------
"""
The hardware for this uart project for a raspberry pi is that the GPIOs
for uart is located at GPIO14 and GPIO15 respective for the TXS(transmitter)
and RXD(reciver).
"""
#--------------------------------------------------------------------
#Import
#--------------------------------------------------------------------
#from msg import DisplayMsg as DM # Import library for standard display messages.
import traceback
import serial # import the serial uart module
import threading # import threading
from uart import Uart # import the uart project
from msg import DisplayMsg as DM
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
#--------------------------------------------------------------------
#METHODS
#--------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + __file__ + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)


name = 'Ubuntu_Uart'
name_rec = 'Dantracker'

port = '/dev/ttyUSB1'

uart = Uart(name)
serial_ports = uart.serial_ports()
print(serial_ports)
serial_port = input("Type the the desired serial port, that you wanted to use, You are only allowed to type one serial port. End by pressing 'Enter'.")
print(serial_port)
