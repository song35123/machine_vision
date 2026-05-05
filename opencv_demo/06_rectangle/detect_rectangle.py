import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("无法加载图像，请检查路径是否正确")
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
        preimeter = cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,0.02*preimeter,True)

        if len(approx) == 4:
            x,y,w,h = cv2.boundingRect(approx)
            rect_area = w * h
            ratio  = area / rect_area
            if ratio > 0.81:
                cv2.drawContours(result,[approx],0,(0,255,0),2)
                cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),0)

                print("检测到疑似矩形")
                print("轮廓面积:", area)
                print("外接矩形面积:", rect_area)
                print("面积比例:", ratio)
                print("矩形坐标 x, y, w, h:", x, y, w, h)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Rectangle Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

