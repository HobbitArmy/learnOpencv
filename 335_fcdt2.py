import cv2
from skimage import measure


img = cv2.imread('ccount.jpg',0)
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = measure.find_contours(img,2)
for cnt in range(len(contours)):
    # 提取与绘制轮廓
    cv2.drawContours(img, contours, cnt, (0, 255, 0),2)

    # 轮廓逼近
    epsilon = 0.01 * cv2.arcLength(contours[cnt], True)
    approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
    corners = len(approx)
    print(cnt)

cv2.imshow('draw_lines.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()


