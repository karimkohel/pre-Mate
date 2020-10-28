import cv2

cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if cv2.waitKey(20) == ord('s'):
        i += 1
        cv2.imwrite(f'frame{i}.jpg',frame)

    elif cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow("Frame", frame)

cap.release()
cv2.destroyAllWindows() 
