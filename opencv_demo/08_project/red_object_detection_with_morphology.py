import cv2
import numpy as np

def detect_red_objects(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Could not read the image.")
        return
    
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

    red_mask = cv2.morphologyEx(red_mask,cv2.MORPH_CLOSE,kernel)

    contours,_ = cv2.findContours(red_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        print("No red object detected.")
        cv2.imshow('Result',result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return
    
    largest = max(contours,key = cv2.contourArea)
    area = cv2.contourArea(largest)

    if area < 50:
        print("Red object detected but below area threshold.")
        cv2.imshow('Result',result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return
    
    x,y,w,h = cv2.boundingRect(largest)
    center_x = x + w//2
    center_y = y + h//2

    image_center_x = image.shape[1] // 2
    image_center_y = image.shape[0] // 2

    offset_x = center_x - image_center_x
    offset_y = center_y - image_center_y
    
    cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle(result,(center_x,center_y),5,(255,0,0),-1)
    cv2.putText(
        result,
        f"Target: ({center_x}, {center_y})",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    cv2.putText(
        result,
        f"Offset: ({offset_x}, {offset_y})",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )
    print("红色目标面积:", area)
    print("红色目标外接矩形 x, y, w, h:", x, y, w, h)
    print("红色目标中心坐标:", center_x, center_y)
    print("图像中心坐标:", image_center_x, image_center_y)

    cv2.imshow("Original Image", image)
    cv2.imshow("Red Mask After Morphology", red_mask)
    cv2.imshow("Detection Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_red_objects("test.jpg")

