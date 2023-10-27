import cv2
import numpy as np

cap = cv2.VideoCapture('videos/AVI25.avi')

lower_bound = np.array([0, 89, 98]) 
upper_bound = np.array([20, 255, 255]) 

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        height, width, _ = frame.shape
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Kırmızı renk aralığını bulma
        mask_red = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        # Canny kenar tespiti
        edges = cv2.Canny(frame, 300, 450)

        # Canny kenarlarını tek bir görüntüde gösterme
        combined = cv2.addWeighted(edges, 0.5, mask_red, 0.5, 0)

        cv2.imshow('Combined', combined)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
