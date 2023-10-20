import cv2

cv2.namedWindow('Aranan Renk', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Aranan Renk', 800, 600)

resim = cv2.imread('images/JPG15.jpg')

orta_nokta_x = resim.shape[1] // 2
orta_nokta_y = resim.shape[0] // 2

(h, w) = resim.shape[:2]

orta_nokta = (w//2, h//2)
cv2.line(resim, (0, orta_nokta_y), (resim.shape[1], orta_nokta_y), (255, 255, 0), 10)
cv2.circle(resim, orta_nokta,30,(), 15)

aranan_renk = resim[orta_nokta_y, orta_nokta_x]

print("Orta yatay çizgideki renk:", aranan_renk)

cv2.imshow('Aranan Renk', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
