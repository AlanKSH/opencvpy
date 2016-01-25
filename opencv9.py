# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('C:\Users\KSH\Pictures\gate.jpg',0)
#低通滤波
result = cv2.blur(img, (5,5))

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)

#低通滤波中每个像素的权重是相同的
#高斯滤波中像素的权重与距中心像素的距离成正比
gaussianResult = cv2.GaussianBlur(img, (5,5), 1.5)
cv2.imshow("Gauss", gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
