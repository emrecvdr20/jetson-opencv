import cv2

# Video dosyasını aç
cap = cv2.VideoCapture('videos/AVI8.avi')

# Toplam çerçeve sayısını al
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Toplam süreyi hesapla (fps ile çarparak)
total_seconds = frame_count / cap.get(cv2.CAP_PROP_FPS)

# Elde edilen bilgileri yazdır
print(f'Toplam Çerçeve Sayısı: {frame_count}')
print(f'Toplam Süre (saniye): {total_seconds}')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

print(length,"\n",width,"\n",height,"\n",fps)

# Video dosyasını kapat
cap.release()
