import cv2
image = cv2.imread("test.jpg")
if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Canny Edge", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
