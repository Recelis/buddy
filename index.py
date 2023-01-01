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
            brightness = vision.get_brightness()
            print(brightness + ' is brightness')
            if brightness > 0:
                # if color is dark then move to rest position
                motorController.move_rest_position()
            else:
                # else color is white then move to view position
                motorController.move_position([60, 180, 90, 180, 0])
            
    except KeyboardInterrupt:
        # turn off everything
        motorController.move_off_position()
        vision.release_camera()

if __name__ == '__main__':
    sys.exit(main())