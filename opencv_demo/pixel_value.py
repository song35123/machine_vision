import cv2
image = cv2.imread("test.jpg")
if image is None:
  print("error")

else:
  print("图像形状：",image.shape)
  pixel = image[0,0]
  print("左上角像素值:",pixel)
  print("B:",pixel[0])
  print("G:",pixle[1])
  print("R:",pixel[2])
