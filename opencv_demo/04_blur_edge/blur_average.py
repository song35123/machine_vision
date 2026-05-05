import cv2

image = cv2.imread("test.jpg")
if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    blur = cv2.blur(image,(5,5))
    cv2.imshow("Original image:",image)
    cv2.imshow("Blur image:",blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
