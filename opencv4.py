# -*- coding: utf-8 -*-
import cv2
import numpy as np

#直方图显示
def calAndDrawHist(image, color):
    """
    第一个参数是需要计算的图像，要用[]圈起来
    第二个采参数是计算直方图的通道，这里使用灰度图计算直方图
    histSize表示直方图分成多少份
    第五个参数表示各个像素的值，0-255像素
    """
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    #找到直方图中的最大值和最小值
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3])
    
    hpt = int(0.9* 256)

    for h in range(256):
        #设置最大峰值为图像高度的90%
        intensity = int(hist[h]*hpt/maxVal)
        cv2.line(histImg, (h,256), (h, 256-intensity), color)

    return histImg

if __name__ == '__main__':
    img = cv2.imread("C:\Users\KSH\Pictures\cat.jpg")
    b, g, r = cv2.split(img)

    histImgB = calAndDrawHist(b, [255,0,0])
    histImgG = calAndDrawHist(g, [0,255,0])
    histImgR = calAndDrawHist(r, [0,0,255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
