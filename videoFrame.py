import cv2

cap = cv2.VideoCapture("videos/AVI8.avi")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_count)
for i in range(frame_count):
    # Bir çerçeve al
    ret, frame = cap.read()

    # Eğer çerçeve alınamazsa döngüden çık
    if not ret:
        break

    # Çerçeveyi konsola yazdır
    print(f"Frame {i}:\n", frame)

# Videoyu serbest bırak
cap.release()
