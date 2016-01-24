#coding=utf-8
import cv2
import numpy as np
#Canny算子

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)
#先用高斯平滑降噪
img = cv2.GaussianBlur(img, (3,3), 0)
#Canny函数，第一个参数是图像，二三为阈值，较大的阈值2检测图像中明显的边缘，阈值1起强化效果
canny = cv2.Canny(img, 50, 150)

cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()