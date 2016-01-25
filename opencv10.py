# -*- coding: utf-8 -*-
import cv2
import numpy as np

"""
使用中值滤波消除噪点
中值滤波器是非线性滤波器，对消除椒盐现象特别有用
medianBlur的第一个参数是图像，第二个参数是滤波器的尺寸
中值滤波不会处理最大最小值，所以不会受到噪声的影响
"""
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] =255
        elif img.ndim ==3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg",0)
result = salt(img, 500)
median = cv2.medianBlur(result, 5)

cv2.imshow("Salt", result)
cv2.imshow("Median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()