# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)


"""
图像中的边缘区域，像素值会突变，对其求导，一阶导数为极值，这是sobel算子的原理
二阶导数为0，laplace计算xy二阶导数之和
"""
#ksize是算子的大小
gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize =3 )
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow("laplacian", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()