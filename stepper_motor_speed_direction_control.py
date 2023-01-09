import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) 
delay = 0.0001

try:
    while(True):
     
        x =7000#int(input("Enter the number of steps  =>  "))
        
        if x > 0 :
            GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
            
            count = x
            while (count > 0): 
                GPIO.output(17, GPIO.HIGH)
                sleep(delay)
                GPIO.output(17, GPIO.LOW) 
                print('pulse count ' + str(count))
                sleep(delay)
                count -= 1
        sleep(1)

        if x > 0 :
            GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
            
            count = x
            while (count > 0): 
                GPIO.output(17, GPIO.HIGH)
                sleep(delay)
                GPIO.output(17, GPIO.LOW) 
                print('pulse count ' + str(count))
                sleep(delay)
                count -= 1 
        
        if x < 0 :
            GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
            count = x
            while (count < 0): 
                GPIO.output(17, GPIO.HIGH)
                sleep(delay)
                GPIO.output(17, GPIO.LOW) 
                print('pulse count ' + str(count))
                sleep(delay)
                count += 1
    
    GPIO.output(27, GPIO.LOW) 
    GPIO.output(17, GPIO.LOW) 
    GPIO.cleanup()
except:
    GPIO.output(27, GPIO.LOW) 
    GPIO.output(17, GPIO.LOW) 
    GPIO.cleanup()










#include <Wire.h>
#include <Adafruit_ADS1015.h>

Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */
//Adafruit_ADS1015 ads;     /* Use this for the 12-bit version */

void setup(void)
{ while (!Serial); 
  delay(1000); // this waits for serial connection to be established
  Serial.begin(9600);
  Serial.println("Hello!");
  
  Serial.println("Getting differential reading from AIN0 (P) and AIN1 (N)");
  Serial.println("ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)");
  
  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                                ADS1015  ADS1115
  //                                                                -------  -------
  // ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  // ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
   //ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
  
  ads.begin();
}

void loop(void)
{
  int16_t results;
  
  /* Be sure to update this value based on the IC and the gain settings! */
  //float   multiplier = 3.0F;    /* ADS1015 @ +/- 6.144V gain (12-bit results) */
  float multiplier = 0.1875F; /* ADS1115  @ +/- 6.144V gain (16-bit results) */

  results = ads.readADC_Differential_0_1();  
    
  Serial.print(" Differential: "); Serial.print(results); Serial.print("("); Serial.print(results * multiplier); Serial.println("mV)");

  delay(1000);
}












