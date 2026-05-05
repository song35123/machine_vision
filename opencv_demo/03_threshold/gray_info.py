import cv2

image = cv2.imread("test.jpg")
if image is None:
    print("图片读取失败，请检查路径是否正确")

else:
  gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  print("原图：",image.shape)
  print("灰度图：",gray.shape)
  print("灰度图数据类型：",gray.dtype)
  cv2.imshow("original image",image)
  cv2.imshow("gray image",gray)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
