import cv2

image = cv2.imread("test.jpg")

if image is None:
  print("error")

else:
  print("图片读取成功")
  print("图片形状：",image.shape)
  print("图片高度：",image.shape[0])
  print("图片宽度：",image.shape[1])
  print("图片通道数：",image.shape[2])
  print("图片数据类型：",image.dtype)
