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




def dodata():
            #print("Do function")
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x03,0x03,0x00,0x00,0x00,0x02,0xC5,0xE9] #temp
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
	                        numstr = str(res)
	                        act1 = numstr[0]
	                        act2 = numstr[1]+numstr[2]+numstr[3]
	                        e1 = float(act1)
	                        e2 = float(act2)
	                        e22 = float(e2/1000)
	                        #print(e22)
	                        e3 = e1 + e22
	                        #print(e1)
	                        #print(e2)
	                        #print(e22)
	                        #print(e3)
	                        return e3
	                       
	                             
	    else :
				print("No Response DO")
				sleep(2)






def orpdata():
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x01,0x03,0x00,0x00,0x00,0x02,0xC4,0x0B] #temp
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				print(data5)
				sleep(3)
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
	                        res = int(hex_value2, 16)
	                        orp = str(res)
	                        #print(orp)
	                        #print("The decimal number associated with hexadecimal string is : " + str(res))
	                        return orp
	                        
	                       
	                        
	                             
	    else :
				print("No Response DO")
				sleep(2)
				




def orptempdata():
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x01,0x03,0x00,0x00,0x00,0x02,0xC4,0x0B] #temp
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				#print(data5)
				sleep(1)
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
	                        numstr = str(res)
	                        act1 = numstr[0]+numstr[1]
	                        act2 = numstr[2]+numstr[3]
	                        e1 = float(act1)
	                        e2 = float(act2)
	                        e22 = float(e2/100)
	                        #print(e22)
	                        phtemp = e1 + e22
	                        #print(e1)
	                        #print(e2)
	                        #print(e22)
	                        #print(e3)
	                        return phtemp
	                        
	                             
	    else :
				print("No Response DO")
				sleep(2)
				

def phtempdata():
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x02,0x03,0x00,0x00,0x00,0x02,0xC4,0x38] #temp
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				#print(data5)
				sleep(1)
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
	                        numstr = str(res)
	                        act1 = numstr[0]+numstr[1]
	                        act2 = numstr[2]+numstr[3]
	                        e1 = float(act1)
	                        e2 = float(act2)
	                        e22 = float(e2/100)
	                        #print(e22)
	                        phtemp = e1 + e22
	                        #print(e1)
	                        #print(e2)
	                        #print(e22)
	                        #print(e3)
	                        return phtemp
	                        
	                             
	    else :
				print("No Response DO")
				sleep(2)
				


def phdata():
            #serialPort = "/dev/ttyUSB0" #2
            serialport2= "/dev/ttyUSB0"
            #port = serial.Serial(serialPort,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
            port2 =serial.Serial(serialport2,baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=None)
	    data=[0x02,0x03,0x00,0x00,0x00,0x02,0xC4,0x38] #temp
	    port2.write(serial.to_bytes(data))
	    time.sleep(.1)
	    if port2.inWaiting()>0:
				data5=[]
				while port2.inWaiting()>0:
						data5.append(binascii.hexlify((port2.read())))
				#print("DO:")
				print(data5)
				sleep(1)
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
	                        numstr = str(res)
	                        act1 = numstr[0]
	                        act2 = numstr[1]+numstr[2]+numstr[3]
	                        e1 = float(act1)
	                        e2 = float(act2)
	                        e22 = float(e2/1000)
	                        #print(e22)
	                        e3 = e1 + e22
	                        #print(e1)
	                        #print(e2)
	                        #print(e22)
	                        #print(e3)
	                        return e3
	                        
	                             
	    else :
				print("No Response ph")
				sleep(2)



while True :
          s = phdata()
          k = phtempdata()
          k2 = orptempdata()
          p = orpdata()
          g = dodata()
          print(str(s) + " phdata")
          print(str(k) + " ph temp")
          print(str(k2) + " orp temp data")
          print(str(p) + "  orp")
          print(str(g) + "  do data")
          sleep(1)
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				


    
               



             	
