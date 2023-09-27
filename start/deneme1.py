import cv2
import numpy as np

def orta_nokta_ciz(frame):
    orta_nokta = (960, 540)  # Ekranın ortasında (960, 540) noktasında bir siyah renk olduğunu belirtiyoruz
    frame = cv2.circle(frame, orta_nokta, 5, (0, 0, 0), -1)  # Siyah bir nokta ekliyoruz
    return frame, orta_nokta

def kayma_hesapla(frame, orta_nokta):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)  # Kenar algılaması parametreleri
    
    # Hough dönüşümü kullanarak çizgileri tespit et
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    
    # Siyah çizgiyi bul
    siyah_cizgi = None
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if frame[y1, x1][0] == 0 and frame[y1, x1][1] == 0 and frame[y1, x1][2] == 0:
                siyah_cizgi = line[0]
                break
    
    return siyah_cizgi

video_cap = cv2.VideoCapture('./videos/video.mp4')

ret, frame = video_cap.read()
frame, orta_nokta = orta_nokta_ciz(frame)
cv2.imshow('Video', frame)
cv2.waitKey(0)

while video_cap.isOpened():
    ret, frame = video_cap.read()
    if not ret:
        break

    # Kayma miktarını hesapla
    siyah_cizgi = kayma_hesapla(frame, orta_nokta)
    
    if siyah_cizgi is not None:
        print(f"Siyah çizgi {siyah_cizgi[0]} piksel kaydı.")
        
        # Ekranın ortasındaki noktadan algılanan çizginin ortasına çizgi çek
        x1, y1, x2, y2 = siyah_cizgi
        orta_x = (x1 + x2) // 2
        orta_y = (y1 + y2) // 2
        frame = cv2.circle(frame, (orta_x, orta_y), 5, (0, 0, 0), -1)  # Algılanan çizginin ortasına siyah bir nokta ekliyoruz
        
        # Kayma miktarını hesapla
        kayma_mesafesi = np.sqrt((orta_nokta[0] - orta_x)**2 + (orta_nokta[1] - orta_y)**2)
        print(f"Verilen koordinattan yapılan kayma: {kayma_mesafesi} piksel")
        
    else:
        print("Siyah çizgi bulunamadı.")

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()
