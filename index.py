from motorcontroller import MotorController
from vision import Vision
import sys
import time


vision = Vision()
motorController = MotorController()

def main():
    state = 'view'
    # detect initial image
    vision.get_image()
    # detect color of image
    brightness = vision.get_brightness()
    vision.THRESHOLD_LIGHTNESS = brightness + 50
    try:
        while(True):
            vision.get_image()
            # detect color of image
            brightness = vision.get_brightness()
            print(brightness)

            if brightness < vision.THRESHOLD_LIGHTNESS:
                # if color is dark then move to rest position
                if state != 'rest':
                    print("move rest position")
                    motorController.move_rest_position()
                    state = 'rest'
                    vision.THRESHOLD_LIGHTNESS = brightness + 50 # reset threshold
                    time.sleep(3)
            else:
                # else color is white then move to view position
                if state != 'view':
                    print("move view position")
                    motorController.move_position(motorController.VIEW_POSITION)
                    state = 'view'
                    time.sleep(3)
            
    except KeyboardInterrupt:
        # turn off everything
        motorController.move_off_position()
        vision.release_camera()

if __name__ == '__main__':
    sys.exit(main())