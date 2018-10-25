import cv2
import numpy as np
img =  cv2.imread('20181023_141530.jpg')
img = cv2.resize(img, None, fx=0.15, fy=0.15)
imCopy = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

image, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imCopy,contours,-1,(255,0,0))
cv2.imshow('draw contours',imCopy)
cv2.imshow("image", image)

biggest = None
max_area = 0
for i in contours:
    area = cv2.contourArea(i)
    if area > 100:
        peri = cv2.arcLength(i,True)
        approx = cv2.approxPolyDP(i,0.02*peri,True)
        if area > max_area and len(approx)==4:
            biggest = approx
            max_area = area
print(biggest)           
print(max_area)           

cv2.waitKey(0)
cv2.destroyAllWindows()
    