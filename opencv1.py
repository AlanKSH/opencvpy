# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:01:01 2016

@author: KSH
"""
import cv2
import numpy as np


#读取图片
img = cv2.imread("C:\Users\KSH\Pictures\cat.jpg")
#新建窗口
cv2.namedWindow("Image")
#图片显示到窗口里
cv2.imshow("Image", img)


#创建图片,用img的大小来创建新图片，img.shape=（541，413，3），
#3表示是RGB图片
emptyImage =np.zeros(img.shape)
#复制原有的图像来获得一幅新图像
emptyImage2 = img.copy()
#获得原图像的副本
emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#emptyImage3[...]=0  

cv2.namedWindow("Image1")
cv2.namedWindow("Image2")
cv2.namedWindow("Image3")
cv2.imshow("Image1", emptyImage)
cv2.imshow("Image2", emptyImage2)
cv2.imshow("Image3", emptyImage3)

#保存图片，jpg可以设置图片质量，越高越好
cv2.imwrite("C:\Users\KSH\Pictures\cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("C:\Users\KSH\Pictures\cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#保存为png，可以设置压缩率，越高图片越差
cv2.imwrite("C:\Users\KSH\Pictures\cat2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite("C:\Users\KSH\Pictures\cat3.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])




#维持窗口，没有这一条图片会一闪而过
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows()