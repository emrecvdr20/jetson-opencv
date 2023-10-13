import cv2
import numpy as np

def find_black_hsv(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])  # Siyahın alt sınırı
    upper_black = np.array([180, 255, 30])  # Siyahın üst sınırı
    mask = cv2.inRange(hsv, lower_black, upper_black)

    return mask

video_path = 'videos/AVI24.avi'  # Video dosya yolu
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    black_mask = find_black_hsv(frame)

    cv2.imshow('Siyah Çizgiler', black_mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
