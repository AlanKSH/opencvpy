import cv2
import numpy as np

img = cv2.imread("C:\Users\KSH\Pictures\cat.jpg")
#把图像按RGB分割
b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Red", r)
cv2.imshow("Green", b)

#分别显示
#b = cv2.split(img)[0]
#g = cv2.split(img)[1]
#r = cv2.split(img)[2]

#合并通道
merged = cv2.merge([b,g,r])
print merged.strides

cv2.imshow("Merged", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()