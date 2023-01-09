# -*- coding: utf-8 -*-
import math
import time
import serial
import binascii
import time
import sys
from time import sleep
from struct import unpack
import ast
from Adafruit_IO import Client
from threading import *
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from datetime import datetime



#################motor
GPIO.setmode(GPIO.BCM) 
GPIO.setup(20,GPIO.OUT)#direction
GPIO.setup(21,GPIO.OUT)#pulse
GPIO.setup(23,GPIO.OUT)#compressor
GPIO.setup(24,GPIO.OUT)#compressor
step = 6000
speed = 0.000001

# compressors initially off
GPIO.output(23,1)
GPIO.output(24,1)
#######################



while True :

            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x01,0x03,0x00,0x00,0x00,0x03,0x05,0xCB] #temp
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				print(data5)
				sleep(5)
	         
	    else :
				print("No Response DO")
				sleep(2)
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				


    
               



             	
