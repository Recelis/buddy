from motorcontroller import MotorController
import sys
import time 

def main():
    motorController = MotorController()
    motorController.move_rest_position()
    time.sleep(10)
    motorController.move_position([60, 180, 270, 130, 0])
    time.sleep(10)
    motorController.off_position()
    return 0

if __name__ == '__main__':
    sys.exit(main())