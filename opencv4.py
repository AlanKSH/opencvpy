import cv2
import numpy as np

#绘制直方图
def calAndDrawHist(image, color):
    """
    第一个参数必须用[]括起来
    第二个参数表示直方图的通道，0代表灰度图
    第三个参数是mask
    第四个参数是，histSize，表示直方图分成多少份
    第五个参数表示直方图各个像素的值
    """
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    #找到直方图中最大最小值
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3])
    
    hpt = int(0.9* 256)

    for h in range(256):
        #设置最大峰值是图像的90%
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
