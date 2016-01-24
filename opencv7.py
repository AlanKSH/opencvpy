#coding=utf-8
import cv2
import numpy as np

#边缘检测，腐蚀和膨胀的变化都发生在边缘，所以只要图像相减，得到的就是边缘。
image = cv2.imread('C:\Users\KSH\Pictures\gate.jpg', 0)
element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dilate = cv2.dilate(image, element)
erode = cv2.erode(image, element)

#图像相减获得边缘，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
result = cv2.absdiff(dilate, erode)

#上面得到的结果是灰度图，将其二值化以便清楚地观察结果
#threshold阈值函数，第二个参数阈值，第三个参数是最大值，第四个参数表示二值化,
#也可以用cv2.THRESH_BINARY_INV直接完成二值并且取反
retval, result = cv2.threshold(result, 40 ,255, cv2.THRESH_BINARY)
#反值，对每一个像素取反
result = cv2.bitwise_not(result)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()