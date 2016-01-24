#coding=utf-8
import cv2

img = cv2.imread('C:\Users\KSH\Pictures\gate.jpg',0)
#低通滤波平滑图像
result = cv2.blur(img, (5,5))

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)

#高斯模糊
#低通滤波与高斯滤波的不同之处在于：
#低通滤波中，滤波器中每个像素的权重是相同的，即滤波器是线性的。
#而高斯滤波器中像素的权重与其距中心像素的距离成比例。
gaussianResult = cv2.GaussianBlur(img, (5,5), 1.5)
cv2.imshow("Gauss", gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
