import time
import RPi.GPIO as GPIO

m11=18
m12=23
m21=24
m22=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 0)
GPIO.output(m12 , 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)

def left_side_forward():
    print "FORWARD LEFT"
    GPIO.output(m21 , 1)
    GPIO.output(m22 , 0)
    time.sleep(.5)
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)

def right_side_forward():
   print "FORWARD RIGHT"
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   time.sleep(.5)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)

def forward():
   print "FORWARD"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)

def left_side_reverse():
   print "BACKWARD LEFT"
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   time.sleep(.5)
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)

def right_side_reverse():
   print "BACKWARD RIGHT"

   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   time.sleep(.5)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)

def reverse():
   print "BACKWARD"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)

def stop():
   print "STOP"
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 0)
 
data=""
while 1:
         data= raw_input('Enter the direction')
         print "Received: %s" % data
         if (data == "F"):    
            forward()
         elif (data == "L"):    
            left_side_forward()
         elif (data == "R"):    
            right_side_forward()
         elif (data == "B"):    
            reverse()
         elif (data == "A"):    
            left_side_reverse()
         elif (data == "P"):    
            right_side_reverse()
         elif data == "S":
            stop()
         elif (data == "Q"):
            print ("Quit")
            break

