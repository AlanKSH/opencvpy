#coding=utf-8
import cv2
import numpy as np

"""
中值滤波处理噪声
由于中值滤波不会处理最大和最小值，所以就不会受到噪声的影响。
相反，如果直接采用blur进行均值滤波，则不会区分这些噪声点，滤波后的图像会受到噪声的影响。
"""
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] =255
        elif img.ndim ==3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg",0)
result = salt(img, 500)
median = cv2.medianBlur(result, 5)

cv2.imshow("Salt", result)
cv2.imshow("Median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()