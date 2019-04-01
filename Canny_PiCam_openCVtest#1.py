import cv2
import numpy as np
import io
from time import sleep
import picamera

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(image, image, mask=detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('Canny Edge', dst)

######Parameter Initialization#######
lowThreshold = 0
i = 100
max_lowThreshold = i
ratio = 3
kernel_size = 3

cv2.namedWindow('Canny Edge')
cv2.createTrackbar('Min threshold', 'Canny Edge', lowThreshold, max_lowThreshold, CannyThreshold)

###########################################
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)#Configuring resolution
    sleep(1)#Initial sleep
    stream = io.BytesIO()#Define the stream which will be received picture info. in next line
    for foo in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        
        image = cv2.imdecode(data, cv2.CV_LOAD_IMAGE_UNCHANGED)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #CannyThreshold(lowThreshold)
        CannyThreshold(cv2.getTrackbarPos('Min threshold', 'Canny Edge'))


        # Truncate the stream to the current position (in case
        # prior iterations output a longer image)
        stream.truncate()
        stream.seek(0)
        
        k=cv2.waitKey(1)
        if k == 27:
            cv2.destroyAllWindows()
            break
        elif k==ord("s"):
            cv2.imwrite("image2.jpg",img)
            cv2.destroyAllWindows()
            break
################################################

"""
#######Main loop in original test######

while True:

    cam.capture(img,'rgb')

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    CannyThreshold(cv2.getTrackbarPos('Min threshold', 'canny demo'))

    k=cv2.waitKey(1)
    if k == 27:

        cv2.destroyAllWindows()
        break
    elif k==ord("s"):

        cv2.imwrite("image2.jpg",img)
        cv2.destroyAllWindows()
        break

cap.release()
"""
