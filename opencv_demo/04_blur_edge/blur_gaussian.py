import cv2

image = cv2.imread("test.jpg")

if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    gaussian = cv2.Gaussianblur(image,(5,5),0)
    cv2.imshow("Original image:",image)
    cv2.imshow("Blur image:",gaussian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
