import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    original = image.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        largest = max(contours,key = cv2.contourArea)
        cv2.drawContours(image,[largest], -1,(0,255,0),3)
        area = cv2.contourArea(largest)
        print("最大轮廓面积：",area)
    else:
        print("没有找到轮廓")
    cv2.imshow("Binary image:",binary)
    cv2.imshow("Largest Contour:",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
