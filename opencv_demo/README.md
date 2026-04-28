# OpenCV 练习

这个文件夹用来存放我学习 OpenCV 时写的一些小实验。

## 当前内容
- read_image.py：读取并显示图片
- gray_image.py：将彩色图片转换为灰度图
- canny_edge.py：使用 Canny 算法进行边缘检测

## 学习目标
- 熟悉 OpenCV 的基础图像处理流程
- 为后续的目标检测与视觉项目打基础

### 1.canny_edge.py
  图片转化为灰度图
  调整canny算子的阈值
  学习cv中的边缘检测操作

### 2.gray_image.py
  学习cv中将图片转化为灰度图
### 3.read_image.py
  学习读取图片
### 4.image_info.py
  读取图片的尺寸大小与通道数和图片类型
### 5.pixel_value.py
  读取图片像素RGB信息
  重点是像素坐标形式与坐标列表元素代表意义
### 6.modify_pixel.py
  更改图片像素的RGB数值
### 7. gray_info.py
查看灰度图与彩色图在 shape 上的区别。

### 8. threshold_binary.py
使用固定阈值进行普通二值化处理。

### 9. threshold_binary_inv.py
使用反向二值化处理图像。

### 10. threshold_otsu.py
使用 Otsu 方法自动计算阈值并完成二值化。

### 11. blur_average.py
使用均值滤波对图像进行平滑处理。

### 12. blur_gaussian.py
使用高斯滤波减少图像噪声。

### 13. blur_median.py
使用中值滤波处理图像噪声。

### 14. gaussian_canny.py
在 Canny 边缘检测前加入高斯滤波，观察边缘检测效果变化。

### 15. find_contours.py
对二值图进行轮廓检测，并将所有轮廓绘制到原图上。

### 16. largest_contour.py
在所有轮廓中找出面积最大的轮廓，并进行绘制。

### 17. bounding_rect.py
为检测到的轮廓绘制外接矩形框。

### 18. approx_polygon.py
使用 `cv2.approxPolyDP()` 对轮廓进行多边形近似，并观察顶点数量。

### 19. detect_quadrilateral.py
通过轮廓近似后的顶点数量，检测图像中的四边形区域。

### 20. draw_corners.py
在检测到的四边形上绘制轮廓和角点坐标。

### 21. detect_rectangle.py
通过四边形顶点数量和面积比例，初步检测疑似矩形区域。

### 22. rectangle_center.py
在检测矩形的基础上，计算并绘制矩形中心点坐标。

### 23. largest_rectangle.py
从多个候选矩形中筛选面积最大的矩形，并输出位置和中心点。