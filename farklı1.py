import cv2
import numpy as np

image = cv2.imread('images/JPG15.jpg')

lower_blue = np.array([170, 50, 50])
upper_blue = np.array([180, 255, 255])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lower_blue, upper_blue)

blue_objects = cv2.bitwise_and(image, image, mask=mask)

gray = cv2.cvtColor(blue_objects, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Mavi Nesneler ve Çizgiler', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
