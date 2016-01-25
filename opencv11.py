# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)

#sobel算子，1，0代表xy方向上的导数，16s表示把图像转换成16bit处理
x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
#重新编程unit8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
#组成两个方向，数字表示权重
dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absX", absX)
cv2.imshow("absY", absY)

cv2.imshow("Result",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
