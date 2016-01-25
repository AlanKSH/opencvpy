# -*- coding: utf-8 -*-
import cv2
import numpy as np
#动态控制Canny检测的阈值大小
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask =detected_edges)
    cv2.imshow('Canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('cannydemo')

#创建控制栏
cv2.createTrackbar('Minthreshold', 'cannydemo', lowThreshold, max_lowThreshold, CannyThreshold)

#CannyThreshold(0)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()