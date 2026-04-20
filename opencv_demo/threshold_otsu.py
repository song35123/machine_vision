import cv2
image = cv2.imread("test.jpg")

if image is None:
  print("图片读取失败，请检查路径是否正确")
else:
  gray = cv2.cvtColer(image,cv2.COLOR_BGR2GRAY)
  ret,otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  print("otsu自动计算出的阈值："ret)
  cv2.imshow("Gray Image", gray)
  cv2.imshow("Otsu Binary Image", otsu)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
