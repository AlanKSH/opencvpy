import cv2
import numpy as np

#����ֱ��ͼ
def calAndDrawHist(image, color):
    """
    ��һ������������[]������
    �ڶ���������ʾֱ��ͼ��ͨ����0����Ҷ�ͼ
    ������������mask
    ���ĸ������ǣ�histSize����ʾֱ��ͼ�ֳɶ��ٷ�
    �����������ʾֱ��ͼ�������ص�ֵ
    """
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    #�ҵ�ֱ��ͼ�������Сֵ
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3])
    
    hpt = int(0.9* 256)

    for h in range(256):
        #��������ֵ��ͼ���90%
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
