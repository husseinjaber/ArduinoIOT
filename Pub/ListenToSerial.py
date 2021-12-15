#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
import time
import csv
import os

ser = serial.Serial('COM3', 115200)
ser.flushInput()

while True:
    file = open("putty.txt","a+")
    ser_bytes = ser.readline()
    #print(ser_bytes)
    decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
    #line = decoded_bytes.decode("utf-8")
    print(decoded_bytes  )
    file.write(decoded_bytes  )
    file.write("\n")
    #close(file)
	
   # try:

        #  with open("putty.log","a") as f:
        #    writer = csv.writer(f,delimiter=",")
        #    writer.writerow([time.time(),decoded_bytes])
    # except:
    #    print("Keyboard Interrupt")
    #    break
