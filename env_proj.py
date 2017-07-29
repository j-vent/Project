
from curiosity_proj import *
from lib_robotis_hack import *
import numpy as np 

Actions = [(x,y,z,w) for x in range(-1,2) for y in range(-1,2) for z in range (-1,2) for w in range (-1,2)]
States = np.linspace(-1.6, 1.6, num=10, endpoint=True, retstep=False, dtype=None)


D = USB2Dynamixel_Device(dev_name="/dev/tty.usbserial-AL01QFD9",baudrate=1000000)#	tty.usbserial-AL01QFD9	
s_list = find_servos(D)
s1 = Robotis_Servo(D,s_list[0])
s2 = Robotis_Servo(D,s_list[1])
s3 = Robotis_Servo(D,s_list[2])
s4 = Robotis_Servo(D,s_list[3])  

    
def returnServos():
        return s1,s2,s3,s4

def init(s1,s2,s3,s4): #state initialization might be in env
        return(s1.read_angle(), s2.read_angle(),s3.read_angle(),s4.read_angle())
    
def takeAction(state,action):
    #s1,s2,s3,s4 = state
        s1.move_angle(action[0])
        s2.move_angle(action[1])
        s3.move_angle(action[2])
        s4.move_angle(action[3])
        observedprime = (s1.read_angle(),s2.read_angle(),s3.read_angle(),s4.read_angle())
        return observedprime

def returnVal():
        return States, Actions
#print (States)