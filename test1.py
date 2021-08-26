
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER1 = 18
GPIO_TRIGGER2 = 17
GPIO_ECHO1 = 24
GPIO_ECHO2 = 25
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
    GPIO.output(GPIO_TRIGGER2, True)
    
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    GPIO.output(GPIO_TRIGGER2, False)
    
 
    StartTime1 = time.time()
    StopTime1 = time.time()
    StartTime2 = time.time()
    StopTime2 = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0 and GPIO.input(GPIO_ECHO2) == 0:
        StartTime1 = time.time()
        StartTime2 = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1 and GPIO.input(GPIO_ECHO2) == 1:
        StopTime1 = time.time()
        StopTime2 = time.time()
 
    # time difference between start and arrival
    TimeElapsed1 = StopTime1 - StartTime1
    TimeElapsed2 = StopTime2 - StartTime2
    
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed1 * 34300) / 2
    distance2= (TimeElapsed2 * 34300) / 2
    
 
    return distance1,distance2
 
if __name__ == '__main__':
    try:
        while True:
            dist1 = distance()
            
            
           print ("Measured Distance = %.1f cm" % dist)
      
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        
        
        
        
        
def a():
  return 5


def b():
   print(a())

  
        
        
        
        
        
        
        
        
        
        
        
        
        
        