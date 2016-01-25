# -*- coding: utf-8 -*-
import cv2
import numpy as np

#自制椒盐图像
def salt(img, n):
    for k in range(n):
        #取随机坐标
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        #ndim，维数，2代表黑白图像
        if img.ndim == 2:
            img[j,i] = 255
        #3代表RGB图像
        elif img.ndim == 3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img

if __name__ == '__main__':
    img = cv2.imread("C:\Users\KSH\Pictures\cat.jpg")
    saltImage = salt(img, 500)
    cv2.imshow("Salt", saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()