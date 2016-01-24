import cv2
import numpy as np
#概率霍夫变换

img = cv2.imread("C:\Users\KSH\Pictures\gate.jpg")

img = cv2.GaussianBlur(img, (3,3), 0)
edges = cv2.Canny(img, 50 ,150, apertureSize=3)
lines = cv2.HoughLines(edges,1,np.pi/180,118)
result = img.copy()

minLineLength = 200
maxLineGap = 15
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('Result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
