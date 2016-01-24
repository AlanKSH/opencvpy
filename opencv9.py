#coding=utf-8
import cv2

img = cv2.imread('C:\Users\KSH\Pictures\gate.jpg',0)
#��ͨ�˲�ƽ��ͼ��
result = cv2.blur(img, (5,5))

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)

#��˹ģ��
#��ͨ�˲����˹�˲��Ĳ�֮ͬ�����ڣ�
#��ͨ�˲��У��˲�����ÿ�����ص�Ȩ������ͬ�ģ����˲��������Եġ�
#����˹�˲��������ص�Ȩ��������������صľ���ɱ�����
gaussianResult = cv2.GaussianBlur(img, (5,5), 1.5)
cv2.imshow("Gauss", gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
