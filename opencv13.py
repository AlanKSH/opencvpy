# -*- coding: utf-8 -*-
import cv2
import numpy as np
#Canny边缘检测

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)
#Canny只能处理灰度图，读取图像要转成灰度图
img = cv2.GaussianBlur(img, (3,3), 0)
#Canny设置最大最小阈值，其中apertureSize默认为3
canny = cv2.Canny(img, 50, 150)

cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()