import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("无法加载图像，请检查路径是否正确")
else:
    result = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

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
            ratio = area / rect_area
            if ratio > 0.81:
                center_x = x + w//2
                center_y = y + h//2

                cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.circle(result,(center_x, center_y), 5, (0,0,255), -1)

                cv2.putText(result, f"Center: ({center_x}, {center_y})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 1)
                print("矩形中心坐标:", (center_x, center_y))
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()