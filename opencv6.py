# -*- coding: utf-8 -*-
import cv2
import numpy as np
"""
开运算和闭运算是指将腐蚀和膨胀按照一定顺序进行处理，不可逆。
闭运算用来链接被分为小块的对象
开运算用来移除图像噪音形成的斑点
先闭后开，得到图像中主要对象
先开后闭，消除破碎对象
"""

img  = cv2.imread('C:\Users\KSH\Pictures\cat.jpg',0)
#生成结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

#闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("close", closed)

#开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("open", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()