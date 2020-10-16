import cv2
from header import *

font = cv2.FONT_HERSHEY_PLAIN
img_color = cv2.imread('star.PNG')
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
inv = cv2.bitwise_not(thresh)
contours, _ = cv2.findContours(inv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.0025* cv2.arcLength(cnt, True), True)
    cv2.drawContours(img_color, [approx], 0, (0, 255, 0), 3)
    tup = (approx[0][0][0], approx[0][0][1]-10)
    shape = getShape(approx)
    cv2.putText(img_color, shape, tup, font, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow("image", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()