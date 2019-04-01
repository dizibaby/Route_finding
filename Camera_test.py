from io import BytesIO
import numpy as np
import cv2
from picamera import PiCamera

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    #dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo', detected_edges)


lowThreshold = 0
i = 100
max_lowThreshold = i
ratio = 3
kernel_size = 3

cam=PiCamera()
img=BytesIO()
cv2.namedWindow('canny demo')
cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)

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
