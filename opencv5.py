#�����븯ʴ
#coding=utf-8
import cv2
import numpy as np
 
img = cv2.imread('C:\Users\KSH\Pictures\cat.jpg',0)
#OpenCV����ĽṹԪ��
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

#��ʴͼ��
eroded = cv2.erode(img,kernel)
#��ʾ��ʴ���ͼ��
cv2.imshow("Eroded Image",eroded);

#����ͼ��
dilated = cv2.dilate(img,kernel)
#��ʾ���ͺ��ͼ��
cv2.imshow("Dilated Image",dilated);
#ԭͼ��
cv2.imshow("Origin", img)

#NumPy����ĽṹԪ��
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(img,NpKernel)
#��ʾ��ʴ���ͼ��
cv2.imshow("Eroded by NumPy kernel",Nperoded);

cv2.waitKey(0)
cv2.destroyAllWindows()