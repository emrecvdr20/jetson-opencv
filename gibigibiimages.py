import cv2
import numpy as np

resim = cv2.imread('images/JPG8.jpg')

cv2.namedWindow('Resim', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resim', 800, 600)

size = resim.shape
print(size)

orta_nokta_x = resim.shape[1] // 2
orta_nokta_y = resim.shape[0] // 2

print(orta_nokta_x)
print(orta_nokta_y)

cv2.line(resim, (0, orta_nokta_y), (resim.shape[1], orta_nokta_y), (0, 255, 0), 10)

hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
alt_kirmizi = np.array([140,30,30])
ust_kirmizi = np.array([190,255,255])

maske = cv2.inRange(hsv_resim, alt_kirmizi, ust_kirmizi)
cv2.circle(resim, (0, 1512), 10, (0, 0, 255), 15)

cv2.circle(resim, (150, 1512), 10, (0, 0, 255), 15)

cv2.circle(resim, (4032, 1512), 10, (0, 0, 255), 15)

konturlar, _ = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if konturlar:
    cv2.circle(resim, (orta_nokta_x, orta_nokta_y), 10, (0, 0, 255), 15)

cv2.imshow('Resim', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
