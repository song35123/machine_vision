import cv2
import numpy as np

def detect_red_objects(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Could not read the image.")
        return
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv,lower_red1,upper_red1)
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2)

    red_mask = mask1 + mask2

    red_mask = cv2.GaussianBlur(red_mask,(5,5),0)
    _, red_mask = cv2.threshold(red_mask,127,255,cv2.THRESH_BINARY)

    contours,hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("没有检测到红色目标")
        cv2.imshow("Original Image", image)
        cv2.imshow("Red Mask", red_mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return
    
    largest = max(contours,key = cv2.contourArea)
    area = cv2.contourArea(largest)

    if area < 50:
        print("检测到的红色目标面积过小，可能是噪声")
        cv2.imshow("Original Image", image)
        cv2.imshow("Red Mask", red_mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return
    
    x,y,w,h = cv2.boundingRect(largest)
    center_x = x + w//2
    center_y = y + h//2

    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle(image,(center_x,center_y),5,(255,0,0),-1)

    print(f"检测到红色目标，中心坐标: ({center_x}, {center_y}), 面积: {area}")
    cv2.imshow("Original Image", image)
    cv2.imshow("Red Mask", red_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    detect_red_objects("test.jpg")
    