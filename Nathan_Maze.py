from robot_control_class import RobotControl
import time
rc = RobotControl()

class Rmove:
    #Why does RobotControl not have ROTATE? 
    #Instructions say to use rotate but it does not exist in robot_control_class
    #Had to use turn
    #Values for speed, time, etc.
    def __init__(self):
        self.move1_speed = 8
        self.move1_time = 1
        self.turn1_speed = 1
        self.turn1_time = 1
        self.laserfront = rc.get_laser(360)
        #Playing with these values
        #Changing them give better or worse results
        #I do not like the way this works!

    def move1(self):
        while self.laserfront > 1:
            rc.move_straight()
            print('Forward distance is', self.laserfront)
            self.laserfront = rc.get_laser(360)
        rc.stop_robot()
        print('Value is less than 1, turning!')

    #This does not fully work
    #Need to incorperate rotate in control_class
    ##def rotate1(self):
    
    def turn1(self):
        right_distance = rc.get_laser(180)
        left_distance = rc.get_laser(560)
        if right_distance < left_distance:
            while self.laserfront < 1:
                print('')
                print('-----------Turning left-----------')
                print('')
                rc.turn('clockwise', self.turn1_speed, self.turn1_time)
                self.laserfront = rc.get_laser(360)
                print('')
                print('###########Done turning###########')
                print('')
        else:
            while self.laserfront < 1:
                print('')
                print('-----------Turning right-----------')
                print('')
                rc.turn('counter-clockwise', self.turn1_speed, self.turn1_time)
                self.laserfront = rc.get_laser(360)
                print('')                
                print('###########Done turning###########')
                print('')
        rc.stop_robot()




































while not rc.ctrl_c:
    rmove = Rmove()
    rmove.move1()
    rmove.turn1()
