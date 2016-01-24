#coding=utf-8
import cv2

"""
�սǼ�⣺
����ʮ����Ԫ�����ͣ�ֻ����ֱ�߱�Ե���ţ��ǲ���
�������νṹ��ʴ��ֻ�йսǴ�������ֱ�߱�Ե����
��X������ԭͼ�񣬽ǵ�����Ҫ�ȱ߶�
���÷��鸯ʴ���ǻָ�ԭ״����Ҫ��ʴ����
���ֻʣ�¹սǴ�
"""
image = cv2.imread("C:\Users\KSH\Pictures\gate.jpg",0)
origin = cv2.imread("C:\Users\KSH\Pictures\gate.jpg")
#����5��5�ĽṹԪ�أ��ֱ�Ϊʮ���Σ����Σ����κ�x��
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
diamond = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

#ʹ��cross����ͼ��
result1 = cv2.dilate(image,cross)
#ʹ�����θ�ʴͼ��
result1 = cv2.erode(result1, diamond)
#ʹ��X����ԭͼ��
result2 = cv2.dilate(image, x)
#ʹ�÷��θ�ʴͼ��
result2 = cv2.erode(result2, square)
#�������������ͼ�������ý�
result = cv2.absdiff(result2,result1)
retval,result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
#��ԭͼ���ð뾶Ϊ5��ԲȦ������
for j in range(result.size):
    y = j / result.shape[0]
    x = j % result.shape[0]

    if result[x,y] == 255:
        cv2.circle(image, (y,x),5,(255,0,0))

cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()