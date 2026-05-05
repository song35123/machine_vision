import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("图片加载失败")
else:
    result = image.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,binary = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500:
            continue
        perimeter = cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,0.02*perimeter,True)
        if len(approx) == 4:
            cv2.drawContours(result,[approx],(0,255,0),2)
            print("找到一个四边形")
    cv2.imshow("result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
