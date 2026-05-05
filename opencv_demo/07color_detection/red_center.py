import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("不存在图片")
else:
    result = image.copy()

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0,50,50])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv,lower_red1,upper_red1)
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2)

    red_mask = mask1 + mask2

    contour,hierarchy = cv2.findContours(red_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(contour) > 0:
        largest = max(contour,key = cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 50:
            x,y,w,h = cv2.boundingRect(largest)

            center_x = x + w//2
            center_y = y + h//2

            cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(result,(center_x,center_y),5,(255,0,0),-1)

            print("红色中心坐标: ({}, {})".format(center_x, center_y))

        else:
            print("红色区域面积过小，无法确定中心坐标")
    else:
        print("未检测到红色区域")
    cv2.imshow("result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


