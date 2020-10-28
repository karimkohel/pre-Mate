import cv2
from header import *

font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(2)

while True:
    ret, img_color = cap.read()
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    inv = cv2.bitwise_not(thresh)
    contours, _ = cv2.findContours(inv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02* cv2.arcLength(cnt, True), True)
        if cv2.contourArea(approx) > 500:
            cv2.drawContours(img_color, [approx], 0, (0, 255, 0), 3)
            tup = (approx[0][0][0], approx[0][0][1]-10)
            shape = getShape(approx)
            cv2.putText(img_color, shape, tup, font, 1, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("image", img_color)
    cv2.imshow("mask", inv)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows()