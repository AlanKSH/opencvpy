# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg",0)
#直方图均衡化
equ = cv2.equalizeHist(img)
cv2.imshow('equ',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()