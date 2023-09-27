import cv2
import numpy as np

#calismalar bu dosyada

def orta_nokta_ciz(frame):
    yukseklik, genislik, _ = frame.shape
    orta_nokta = (genislik // 2, yukseklik // 2)
    frame = cv2.circle(frame, orta_nokta, 5, (0, 255, 0), -1)
    #print(orta_nokta) #(960x540)
    return frame, orta_nokta


def kayma_hesapla(frame, orta_nokta):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 50, 150)
    
    # Hough dönüşümü kullanarak çizgileri tespit et
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    
    # Orta çizgiyi bul
    orta_cizgi = None
    if lines is not None:
        orta_cizgi = lines[0][0]
    
    return orta_cizgi

video_cap = cv2.VideoCapture('./videos/video.mp4')

def siyah_rengi_bul(frame):
    lower_siyah = np.array([0, 0, 0])
    upper_siyah = np.array([30, 30, 100])

    mask = cv2.inRange(frame, lower_siyah, upper_siyah)
    return mask


while video_cap.isOpened():
    ret, frame = video_cap.read()
    if not ret:
        break

    frame, orta_nokta = orta_nokta_ciz(frame)
    
    # Kayma miktarını hesapla
    kayma = kayma_hesapla(frame, orta_nokta)
    
    if kayma is not None:
        print(f"Ortadaki siyah çizgi {kayma[0]} piksel kaydı.")
        
        # Siyah çizginin ortasına yeşil bir nokta ekle
        x1, y1, x2, y2 = kayma
        orta_x = (x1 + x2) // 2
        orta_y = (y1 + y2) // 2
        frame = cv2.circle(frame, (orta_x, orta_y), 5, (0, 255, 0), -1)
        
        # Yeşil noktadan siyah çizgiye çizgi çek
        frame = cv2.line(frame, orta_nokta, (orta_x, orta_y), (0, 0, 255), 2)
    else:
        print("Siyah çizgi bulunamadı.")

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()
