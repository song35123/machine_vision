import cv2

image = cv2.imread("test.jpg")
if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2_GRAY)
    gaussian = cv2.GaussianBlur(gray,(5,5),0)
    edges = cv2.Canny(gaussian,100,200)
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Gaussian Gray", gaussian)
    cv2.imshow("Canny Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
