#coding=utf-8
import cv2
import numpy as np
#Canny����

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)
#���ø�˹ƽ������
img = cv2.GaussianBlur(img, (3,3), 0)
#Canny��������һ��������ͼ�񣬶���Ϊ��ֵ���ϴ����ֵ2���ͼ�������Եı�Ե����ֵ1��ǿ��Ч��
canny = cv2.Canny(img, 50, 150)

cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()