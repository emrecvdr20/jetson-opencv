import cv2
import numpy as np

# Resmi yükle
image_path = "images/image1.jpeg"  # Kullanmak istediğiniz resmin dosya yolu
image = cv2.imread(image_path)

# Görüntüyü HSV renk uzayına çevir
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Kırmızı renk aralığını tanımla (HSV)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Siyah renk aralığını tanımla (HSV)
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])  # Siyah rengin alt ve üst sınırları

# Renk maskelemeleri
red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
black_mask = cv2.inRange(hsv_image, lower_black, upper_black)

# Kırmızı bölgelerin merkezini bul
red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in red_contours:
    red_moments = cv2.moments(contour)
    if red_moments["m00"] != 0:
        red_cx = int(red_moments["m10"] / red_moments["m00"])
        red_cy = int(red_moments["m01"] / red_moments["m00"])
        cv2.circle(image, (red_cx, red_cy), 5, (0, 0, 255), -1)  # Kırmızı nokta

# Siyah bölgelerin merkezini bul
black_contours, _ = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in black_contours:
    black_moments = cv2.moments(contour)
    if black_moments["m00"] != 0:
        black_cx = int(black_moments["m10"] / black_moments["m00"])
        black_cy = int(black_moments["m01"] / black_moments["m00"])
        cv2.circle(image, (black_cx, black_cy), 5, (0, 255, 0), -1)  # Yeşil nokta

        # Siyah noktadan kırmızı noktaya çizgi çiz
        cv2.line(image, (black_cx, black_cy), (red_cx, red_cy), (255, 0, 0), 2)

        # Mesafeyi hesapla
        distance = np.sqrt((red_cx - black_cx)**2 + (red_cy - black_cy)**2)
        text = f"Mesafe: {distance:.2f} piksel"
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Resmi göster
cv2.imshow("Distance Calculation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
