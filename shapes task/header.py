import cv2

def getShape(approx):
    
    pts = len(approx)
    print(pts)

    if pts == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ratio = w / float(h)
        shape = "square" if ratio >= 0.90 and ratio <= 1.1 else "rectangle"

    elif pts == 3:
        shape = "triangle"

    elif 4 < pts < 50:
        shape = "circle" if pts > 25 else "star"
    else:
        shape = "N/A"

    return shape