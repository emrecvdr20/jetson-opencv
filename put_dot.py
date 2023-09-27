import cv2


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
    
    # Görüntünün boyutlarını al
    height, width, _ = frame.shape
    
    # Görüntünün orta noktasını hesapla
    center_x = width // 2
    center_y = height // 2
    
    # Referans noktasını çiz
    cv2.circle(frame, (center_x, center_y), 10, (255, 0, 0), -1)
    
    # Görüntüyü göster
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
