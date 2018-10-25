import cv2
import numpy as np


img = cv2.imread('20181023_140526.jpg',0)
rsz_img = cv2.resize(img, None, fx=0.15, fy=0.15)
edges = cv2.Canny(rsz_img,100,200)

# cv2.imshow("original", rsz_img)
# cv2.imshow("Test", edges)
image, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


biggest = None
max_area = 0
for i in contours:
        area = cv2.contourArea(i)
        print(area)
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
