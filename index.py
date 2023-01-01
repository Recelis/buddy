from motorcontroller import MotorController
from vision import Vision
import sys
import time


vision = Vision()
motorController = MotorController()

def main():
    motorController.move_rest_position()
    time.sleep(10)
    while(True):
        vision.get_image()
        
        motorController.move_position([60, 180, 270, 180, 0])
        time.sleep(10)
        motorController.move_off_position()
        time.sleep(10)

if __name__ == '__main__':
    motorController.move_off_position()
    vision.release_camera()
    sys.exit(main())