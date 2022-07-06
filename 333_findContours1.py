import cv2
import numpy as np


img = cv2.imread('ccount.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 50, 200)

cv2.approxPolyDP()

minLineLength = 60
maxLineGap = 40
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 10,minLineLength)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('edges', edges)
cv2.imshow('draw_lines.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()


