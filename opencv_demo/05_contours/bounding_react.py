import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    result = image.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Binary image:",binary)
    cv2.imshow("Bounding Rectangles:",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()