import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("不存在图片")
else:
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    print("hsv shape:",hsv.shape)
    print("original image shape:",image.shape)

    cv2.imshow("hsv",hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()