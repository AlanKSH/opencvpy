#coding=utf-8
import cv2
import numpy as np

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)

#sobel,1,0表示分别对xy方向上求导，cv_16s表示使用16位有符号的数据类型
x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
#转回unit8格式
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
#将两个方向的图像合并，数字表示权重
dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absX", absX)
cv2.imshow("absY", absY)

cv2.imshow("Result",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
