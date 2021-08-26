import sys
import time
import RPi.GPIO as gpio


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(9, gpio.OUT)
    gpio.setup(10, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    gpio.setup(8, gpio.OUT)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    
    
    
def forward(tf):
    init()
    gpio.output(9,False)
    gpio.output(25,False)
    gpio.output(5,False)
    gpio.output(12,False)
    gpio.output(10,True)
    gpio.output(8,True)
    gpio.output(6,True)
    gpio.output(13,True)
    
    time.sleep(tf)
    gpio.cleanup()


def reverse(tf):
    init()
    gpio.output(9,True) 
    gpio.output(25,True)
    gpio.output(5,True)
    gpio.output(12,True)
    gpio.output(10,False)
    gpio.output(8,False)
    gpio.output(6,False)
    gpio.output(13,False)
    time.sleep(tf)
    
    gpio.cleanup()
    
def right(tf):
     init()
    
     gpio.output(9,False)
     gpio.output(10,True)
     gpio.output(25,False)
     gpio.output(8,True)
     time.sleep(tf)
     
     gpio.cleanup()


def left(tf):
     init()
     gpio.output(9,True)
     gpio.output(10,False)
     gpio.output(25,True)
     gpio.output(8,False)
     gpio.output(5,False)
     gpio.output(6,True)
     gpio.output(12,False)
     gpio.output(13,True)
     time.sleep(tf)
     gpio.cleanup()
    
    
def halt(tf):
    init()
    pass
   
    
    
    
print("forward")
forward(2)
reverse(2)
right(4)
left(4)
    

