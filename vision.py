import cv2

class Vision():
    def __init__( self ):
        super().__init__( )
        # initialize the camera
        self.cam = cv2.VideoCapture(0)
        
    THRESHOLD_LIGHTNESS = 0

    def get_image(self):
        # Capture frame-by-frame
        ret, frame = self.cam.read()

        # Display the resulting frame
        cv2.imshow('Video Test',frame)
        pass

    def get_lightness(self):
        pass

    def get_distance(self):
        pass

    def get_face_coordinates(self):
        pass

    def release_camera(self):
        # When everything done, release the capture
        self.cam.release()
        cv2.destroyAllWindows()