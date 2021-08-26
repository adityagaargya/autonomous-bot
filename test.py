
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins

GPIO_TRIGGER1 = 2
GPIO_TRIGGER2 = 3
GPIO_TRIGGER3 = 1
GPIO_ECHO1 = 14
GPIO_ECHO2 = 15
GPIO_ECHO3 = 7
# 
# Initialization functions

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
    
    

    
def init_motor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    
   
 
def distance(num):
    # set Trigger to HIGH
   
    if num == 1:
        GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
        time.sleep(1)
        GPIO.output(GPIO_TRIGGER1, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
    # save StartTime
        while GPIO.input(GPIO_ECHO1) == 0:
            StartTime = time.time()
 
    # save time of arrival
        while GPIO.input(GPIO_ECHO1) == 1:
            StopTime = time.time()
 
    # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
 
    

    
    if num == 2:
        GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
        time.sleep(1)
        GPIO.output(GPIO_TRIGGER2, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
    # save StartTime
        while GPIO.input(GPIO_ECHO2) == 0:
            StartTime = time.time()
 
    # save time of arrival
        while GPIO.input(GPIO_ECHO2) == 1:
            StopTime = time.time()
 
    # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        
        
        
        
    if num == 3:
        GPIO.output(GPIO_TRIGGER3, True)
 
    # set Trigger after 0.01ms to LOW
        time.sleep(1)
        GPIO.output(GPIO_TRIGGER3, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
    # save StartTime
        while GPIO.input(GPIO_ECHO3) == 0:
            StartTime = time.time()
 
    # save time of arrival
        while GPIO.input(GPIO_ECHO3) == 1:
            StopTime = time.time()
 
    # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        


 
    return distance


    
# Motor Functions
    
def forward(tf):
    init_motor()
    GPIO.output(9,False)
    GPIO.output(25,False)
    GPIO.output(5,False)
    GPIO.output(12,False)
    GPIO.output(10,True)
    GPIO.output(8,True)
    GPIO.output(6,True)
    GPIO.output(13,True)
    
    time.sleep(tf)
    GPIO.cleanup()


def reverse(tf):
    init_motor()
    GPIO.output(9,True) 
    GPIO.output(25,True)
    GPIO.output(5,True)
    GPIO.output(12,True)
    GPIO.output(10,False)
    GPIO.output(8,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    time.sleep(tf)
    
    GPIO.cleanup()
    
def right(tf):
     init_motor()
    
     GPIO.output(9,False)
     GPIO.output(10,True)
     GPIO.output(25,False)
     GPIO.output(8,True)
     time.sleep(tf)
     GPIO.cleanup()


def left(tf):
     init_motor()
     GPIO.output(9,True)
     GPIO.output(10,False)
     GPIO.output(25,True)
     GPIO.output(8,False)
     time.sleep(tf)
     GPIO.cleanup()
    

 
if __name__ == '__main__':
    try:
        while True:
            right_wall = distance(1)
            front_wall = distance(2)
            left_wall = distance(3)
#            
            print ("Measured Distance = %.1f cm from right sensor" % right_wall)
            print ("Measured Distance = %.1f cm from front sensor" % front_wall)
            print ("Measured Distance = %.1f cm from left sensor" % left_wall)
#           time.sleep(1)
#           while sensor1 > 20:
#                forward()
#  
#                
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()