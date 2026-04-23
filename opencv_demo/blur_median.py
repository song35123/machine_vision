import cv2
image = cv2.imread("test.jpg")
if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    median = cv2.medianBlur(image,5)
    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blur", median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
