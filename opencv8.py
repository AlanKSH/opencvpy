# -*- coding: utf-8 -*-
import cv2

"""
拐点检测
先用十字形膨胀，边缘扩张，但是角不变
再用菱形腐蚀，角收缩，边缘不变
用X形膨胀原图，角膨胀比边多
方块腐蚀，角恢复，边腐蚀更多
两图相减，只留下角
"""
image = cv2.imread("C:\Users\KSH\Pictures\gate.jpg",0)
origin = cv2.imread("C:\Users\KSH\Pictures\gate.jpg")
#生成结构元素，分别为十字、菱形、方形、和X形
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

#cross膨胀
result1 = cv2.dilate(image,cross)
#菱形腐蚀
result1 = cv2.erode(result1, diamond)
#X膨胀
result2 = cv2.dilate(image, x)
#方形腐蚀
result2 = cv2.erode(result2, square)
#两幅闭运算图像相减获得角
result = cv2.absdiff(result2,result1)
#获得二值图
retval,result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
#用半径为5的圆圈标出点
for j in range(result.size):
    y = j / result.shape[0]
    x = j % result.shape[0]

    if result[x,y] == 255:
        cv2.circle(image, (y,x),5,(255,0,0))

cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()