import cv2

image = cv2.imread("test.jpg")
if image is None:
  print("图片读取失败，请检查路径是否正确")

else:
  height = image.shape[0]
  width = image.shape[1]
  half_h = height/2
  half_w = width/2
  image[(half_h - 50):(half_h + 50),(half_w - 50):(half_w + 50)] = [0,255,0]
  cv2.imshow("Modified Image", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  # image[0:100,0:100] = [0,0,255]
  # cv2.imshow("Modified Image", image)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
