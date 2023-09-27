import cv2
import numpy as np


def gstreamer_pipeline(
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink drop=True"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# Kamera başlatma
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Deri rengi aralığı
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Maske oluştur
    skin_mask = cv2.inRange(hsv_frame, lower_skin, upper_skin)
    
    # Maskeyi uygula
    skin_segmented = cv2.bitwise_and(frame, frame, mask=skin_mask)
    
    # Görüntüyü göster
    cv2.imshow('Skin Segmented', skin_segmented)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
