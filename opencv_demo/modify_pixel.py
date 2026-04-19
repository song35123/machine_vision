import cv2

image = cv2.imread("test.jpg")
if image is None:
  print("图片读取失败，请检查路径是否正确")

else:
  image[0:100,0:100] = [0,0,255]
  cv2.imshow("Modified Image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
