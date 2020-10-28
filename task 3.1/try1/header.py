import cv2

def getShape(approx):
    
    pts = len(approx)
    
    if pts == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ratio = w / float(h)
        #       square                                                   rectangle
        shape = "4th Century BC" if ratio >= 0.90 and ratio <= 1.1 else "6th Century BC"

    elif pts == 3:
        #       trinagle
        shape = "3rd Century BC"

    elif 4 < pts < 70:
        #       circle                              star
        shape = "2nd Century BC" if pts > 30 else "5th Century BC"
    else:
        shape = "N/A"

    return shape