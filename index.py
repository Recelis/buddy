from motorcontroller import MotorController
from vision import Vision
import sys
import time


vision = Vision()
motorController = MotorController()

def main():
    try:
        time.sleep(10)
        while(True):
            vision.get_image()
            # detect color of image

            # if color is dark then move to rest position
            motorController.move_rest_position()
            time.sleep(10)
            # else color is white then move to view position
            motorController.move_position([60, 180, 270, 180, 0])
            time.sleep(10)
    except KeyboardInterrupt:
        motorController.move_off_position()
        vision.release_camera()
        
if __name__ == '__main__':
    # turn off everything
    sys.exit(main())