import cv2
import math
from PIL import ImageStat
class Vision():
    def __init__( self ):
        super().__init__( )
        # initialize the camera
        self.cam = cv2.VideoCapture('/dev/video0')
        self.frame = None
        
    THRESHOLD_LIGHTNESS = 0

    def get_image(self):
        # Capture frame-by-frame
        ret, frame = self.cam.read()

        # Display the resulting frame
        print('video test')
        cv2.imshow('Video Test', frame)
        cv2.waitKey(1)
        self.frame = frame

    def get_brightness(self):
        stat = ImageStat.Stat(self.frame)
        r,g,b = stat.mean
        return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

    def get_distance(self):
        pass

    def get_face_coordinates(self):
        pass

    def release_camera(self):
        # When everything done, release the capture
        self.cam.release()
        cv2.destroyAllWindows()