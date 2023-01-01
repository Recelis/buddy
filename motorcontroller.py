from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)



class MotorController():
    def __init__( self ):
        super().__init__( )
        self.motor_0 = kit.servo[0] # end effector motor
        self.motor_0.actuation_range = 180
        self.motor_1 = kit.servo[1]
        self.motor_1.actuation_range = 180
        self.motor_2 = kit.servo[2] # max is 90
        self.motor_2.actuation_range = 360
        self.motor_3 = kit.servo[3]
        self.motor_3.actuation_range = 180 # range is 30, 180
        self.motor_4 = kit.servo[4] # base motor
        self.motor_4.actuation_range = 360

        self.REST_POSITION = [60, 180, 350, 180, 180]
        self.VIEW_POSITION = [60, 60, 90, 180, 0]
        self.TURN_OFF = [None, None, None, None, None]

    # functions
    
    def move_position(self, position):
        # time sleep to limit current draw during each motor 
        self.motor_0.angle = position[0]
        time.sleep(1)
        self.motor_1.angle = position[1]
        time.sleep(2)
        self.motor_2.angle = position[2]
        time.sleep(1)
        self.motor_3.angle = position[3]
        time.sleep(1)
        self.motor_4.angle = position[4]
        print(position)


    def move_rest_position(self):
        self.move_position(self.REST_POSITION)

    def move_off_position(self):
        self.move_position(self.TURN_OFF)
        self.motor_3.fraction = None
        self.motor_4.fraction = None