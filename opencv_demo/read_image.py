import cv
image = cv.imread("test.jpg")

if image is None:
  print("图片读取失败，请检查路径是否正确")
else:
  cv2.imshow("Image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
