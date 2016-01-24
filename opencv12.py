#coding=utf-8
import cv2
import numpy as np

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg", 0)

#������˹���ӣ�ksize�����ӵĴ�С
"""
ͼ���еı�Ե��������ֵ�ᷢ������Ծ��������Щ�����󵼣�����һ�׵����ڱ�Եλ��Ϊ��ֵ�������Sobel����ʹ�õ�ԭ������ֵ�����Ǳ�Ե��
Laplace����ʵ�ֵķ���������Sobel ���Ӽ������x��y�����������
"""
gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize =3 )
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow("laplacian", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()