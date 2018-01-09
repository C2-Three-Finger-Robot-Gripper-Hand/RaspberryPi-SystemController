#!/usr/bin/env python
import minimalmodbus
import time
import sys

instrument = minimalmodbus.Instrument('/dev/serial0', 1, minimalmodbus.MODE_ASCII) # port name, slave address (in decimal)
instrument.serial.baudrate = 115200
instrument.serial.timeout=0.2

##First calibrate

#try:
#	instrument.write_register(3, 2) # Registernumber, calibrating
#	print("Calibrating...")
#except Exception as e:
#  	print(e)


#answer = input("Proceed: ")

#try:
#  instrument.write_register(3, 0) # Registernumber, running
#  print("Running...")
#except Exception as e:
#  print(e)

motor = 0
degree = 0
while(1):
  try:
    motor = input("Motor number: ")
    degree = input("Enter degrees: ")
    instrument.write_register(motor - 1, degree) # Registernumber, value
    print("Writed data: " + str(val))
  except Exception as e:
      print(e)
  time.sleep(1)
  
  try:
    degree = instrument.read_register(motor, 0) # Registernumber, number of decimals
    print("Current degrees: " + str(degree))
  except Exception as e:
    print(e)
  time.sleep(1)

