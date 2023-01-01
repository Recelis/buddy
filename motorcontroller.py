from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

REST_POSITION = [60, 180, 180, 90, 0]
VIEW_POSITION = [60, 0, 270, 180, 0]
TURN_OFF = [None, None, None, None, None]

class MotorController():
    def __init__( self ):
        super().__init__( )
        self.motor_0 = kit.servo[0] # end effector motor
        self.motor_0.actuation_range = 180
        self.motor_1 = kit.servo[1]
        self.motor_1.actuation_range = 180
        self.motor_2 = kit.servo[2] # max is 90
        self.motor_2.actuation_range = 270
        self.motor_3 = kit.servo[3]
        self.motor_3.actuation_range = 180 # range is 30, 180
        self.motor_4 = kit.servo[4] # base motor
        self.motor_4.actuation_range = 360

    # functions
    
    def move_position(self, position):
        self.motor_0.angle = position[0]
        self.motor_1.angle = position[1]
        self.motor_2.angle = position[2]
        self.motor_3.angle = position[3]
        self.motor_4.angle = position[4]


    def move_rest_position(self):
        self.move_position(REST_POSITION)

    def move_off_position(self):
        self.move_position(TURN_OFF)
        self.motor_3.fraction = None
        self.motor_4.fraction = None