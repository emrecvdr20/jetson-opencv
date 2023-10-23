import cv2
import numpy as np

# Videoyu aç
cap = cv2.VideoCapture('videos/AVI11.avi')  # 'your_video.mp4' dosya adını ve yolunu belirtmelisiniz

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # Kenarları tespit et
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Hough dönüşümünü uygula
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

    # Çizgileri çiz
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Görüntüyü göster
    cv2.imshow('Frame', frame)

    # Çıkış için q tuşuna basılmasını kontrol et
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Videoyu serbest bırak
cap.release()

# Pencereleri kapat
cv2.destroyAllWindows()