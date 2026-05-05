import cv2
import numpy as np

image = cv2.imread("test.jpg")

if image is None:
    print("Could not read the image.")

else:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    kernel = np.ones((5,5,),np.uint8)

    dilated = cv2.dilate(binary,kernel,iterations=1)
    cv2.imshow('Original',binary)
    cv2.imshow('Dilated',dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()