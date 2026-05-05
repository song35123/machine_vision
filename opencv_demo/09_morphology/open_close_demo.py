import cv2
import numpy as np

image = cv2.imread("test.jpg")

if image is None:
    print("Could not read the image.")
else:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    kernel = np.ones((5,5,),np.uint8)

    opening = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)

    cv2.imshow('Original',binary)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()