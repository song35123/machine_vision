import cv2
import numpy as np

image = cv2.imread("test.jpg")

if image is None:
    print("Could not read the image.")
else:
    result = image.copy()

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 80, 80])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 80, 80])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv,lower_red1,upper_red1)
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2)
    mask = mask1 + mask2

    kernel = np.ones((5,5),np.uint8)

    red_mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    contours,_ = cv2.findContours(red_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest = max(contours,key = cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 500:
            x,y,w,h = cv2.boundingRect(largest)
            center_x = x + w//2
            center_y = y + h//2
            cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(result,(center_x,center_y),5,(255,0,0),-1)
            print(f"Red object detected at ({center_x}, {center_y}) with area {area}")
        else:
            print("Red object detected but below area threshold.")
    else:
        print("No red object detected.")
    cv2.imshow('Result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()