#coding=utf-8
#�������������
import cv2
import numpy as np
"""
������ͱ�������ǽ���ʴ�����Ͱ���һ���Ĵ�����д���
�������������ӱ����Ϊ���С��Ķ��󣬶������������Ƴ���ͼ�������γɵİߵ㡣
��ˣ�ĳЩ����¿��������������������㡣
���һ����ֵͼ����ʹ�ñ�����Ϳ����㣬�����ͼ���е���Ҫ����
ͬ�������������ͼ���е���������ͼ���еġ�С�㡱����Ҳ���Զ�ͼ�����ÿ�������ñ����㣬��������Ҳ������һЩ����Ķ���
"""

img  = cv2.imread('C:\Users\KSH\Pictures\cat.jpg',0)
#����ṹԪ��
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

#������
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#��ʾ��ʴ���ͼ��
cv2.imshow("close", closed)

#������
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#��ʾ��ʴ���ͼ��
cv2.imshow("open", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()