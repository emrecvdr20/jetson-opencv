import cv2
import numpy as np

# Resmi yükleyin
image = cv2.imread('images/image2.jpeg')

# Resmi gri tonlamada işleyin
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kırmızı renk segmentasyonu
lower_red = np.array([0, 0, 200])  # Kırmızı rengin alt sınırı
upper_red = np.array([50, 50, 255])  # Kırmızı rengin üst sınırı
mask_red = cv2.inRange(image, lower_red, upper_red)

# Siyah renk segmentasyonu
lower_black = np.array([0, 0, 0])  # Siyah rengin alt sınırı
upper_black = np.array([30, 30, 30])  # Siyah rengin üst sınırı
mask_black = cv2.inRange(image, lower_black, upper_black)

# Kırmızı çizginin sınırlarını bulma
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_contour = max(contours_red, key=cv2.contourArea)

# Siyah çizginin sınırlarını bulma
contours_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
black_contour = max(contours_black, key=cv2.contourArea)

# Kırmızı çizginin merkezini ve siyah çizginin merkezini bulma
red_center = np.mean(red_contour, axis=0)
black_center = np.mean(black_contour, axis=0)

# İki merkez arasındaki mesafeyi hesaplama
distance = np.linalg.norm(red_center - black_center)

print("Kırmızı çizgiden siyah çizgiye olan mesafe:", distance)
