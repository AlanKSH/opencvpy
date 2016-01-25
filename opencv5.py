# -*- coding: utf-8 -*-
#膨胀与腐蚀

import cv2
import numpy as np
 
img = cv2.imread('C:\Users\KSH\Pictures\cat.jpg',0)
#生成结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

#腐蚀
eroded = cv2.erode(img,kernel)
cv2.imshow("Eroded Image",eroded);

#膨胀
dilated = cv2.dilate(img,kernel)
cv2.imshow("Dilated Image",dilated);
cv2.imshow("Origin", img)

#NumPy生成结构元素
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(img,NpKernel)
cv2.imshow("Eroded by NumPy kernel",Nperoded);

cv2.waitKey(0)
cv2.destroyAllWindows()