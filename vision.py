import cv2
class Vision():
    def __init__( self ):
        super().__init__( )
        # initialize the camera
        self.cam = cv2.VideoCapture('/dev/video0')
        self.frame = None
        
    THRESHOLD_LIGHTNESS = 150

    def get_image(self):
        # Capture frame-by-frame
        ret, frame = self.cam.read()

        # Display the resulting frame
        print('video test')
        # cv2.imshow('Video Test', frame)
        # cv2.waitKey(1)
        self.frame = frame

    def get_brightness(self):
        hsv_img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        mean = hsv_img[...,2].mean()
        return mean

    def get_distance(self):
        pass

    def get_face_coordinates(self):
        pass

    def release_camera(self):
        # When everything done, release the capture
        self.cam.release()
        cv2.destroyAllWindows()