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

def dodata() :
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x01,0x03,0x00,0x00,0x00,0x03,0x05,0xCB]
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				print(data5)
	                        dodata1 = data5[5]
	                        dodata2 = data5[6]
	                        sum1 = dodata1 + dodata2
	                        an_integer1 = int(dodata1, 16)
	                        an_integer2 = int(dodata2, 16)
	                        an_integer3 = int(sum1, 16)
	                        hex_value1 = hex(an_integer1)
	                        hex_value2 = hex(an_integer2)
	                        hex_value3 = hex(an_integer3)
	                        #print(hex_value1)
	                        #print(hex_value2)
	                        #print(hex_value3)
	                        res = int(hex_value3, 16)
	                        #print("The decimal number associated with hexadecimal string is : " + str(res))
	                        #print(res)
	                        phdata = res*0.01
	                        #print(phdata)
	                        return phdata
	                        
	                             
	    else :
				print("No Response DO")
				sleep(2)
		

def tempdata() :
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x01,0x03,0x00,0x00,0x00,0x03,0x05,0xCB] 
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				print(data5)
	                        dodata1 = data5[3]
	                        dodata2 = data5[4]
	                        sum1 = dodata1 + dodata2
	                        an_integer1 = int(dodata1, 16)
	                        an_integer2 = int(dodata2, 16)
	                        an_integer3 = int(sum1, 16)
	                        hex_value1 = hex(an_integer1)
	                        hex_value2 = hex(an_integer2)
	                        hex_value3 = hex(an_integer3)
	                        #print(hex_value1)
	                        #print(hex_value2)
	                        #print(hex_value3)
	                        res = int(hex_value3, 16)
	                        #print("The decimal number associated with hexadecimal string is : " + str(res))
	                        #print(res)
	                        tempdata = res*0.1
	                        #print(phdata)
	                        return tempdata
	                        
	                             
	    else :
				print("No Response DO")
				sleep(2)		


while True :
           kk = dodata()
           kk2 = tempdata()
           print(kk)
           print(kk2)
           sleep(4)

				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				


    
               



             	
