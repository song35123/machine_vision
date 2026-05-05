import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("无法加载图像，请检查路径是否正确")
else:
    result = image.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    largest_area = 0
    largest_contour = None

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
            if ratio > 0.81 and area > largest_area:
                largest_area = area
                largest_contour = approx
    if largest_contour is not None:
        x,y,w,h,approx = largest_area
        center_x = x + w//2
        center_y = y + h//2
        cv2.drawContours(result, [largest_contour], -1, (0,255,0), 2)
        cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(result,(center_x, center_y), 5, (0,0,255), -1)
        print("最大矩形面积:", largest_area)
        print("最大矩形坐标 x, y, w, h:", x, y, w, h)
        print("最大矩形中心:", center_x, center_y)
    else:
        print("没有检测到符合条件的矩形")

    cv2.imshow("Largest Rectangle", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()