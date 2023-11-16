import cv2
import numpy as np
import time

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

cap = cv2.VideoCapture('videos/AVI17.avi')

pixelCm = 0.027

start_time = time.time()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        M = cv2.moments(max(contours, key=cv2.contourArea))
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        center_x = frame.shape[1] // 2
        center_y = frame.shape[0] // 2
        
        sapma_x = cX - center_x
        sapma_y = cY - center_y
        

        distance_cm = ((sapma_x * pixelCm) ** 2 + (sapma_y * pixelCm) ** 2) ** 0.5
        
        cv2.line(frame, (center_x, 0), (center_x, frame.shape[0]), (0, 255, 0), 2)
        cv2.line(frame, (0, center_y), (frame.shape[1], center_y), (0, 255, 0), 2)
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
        cv2.line(frame, (center_x, center_y), (cX, cY), (255, 0, 0), 2)
        
        print(f"Sapma X: {sapma_x}, Sapma Y: {sapma_y}")
        
    
        cv2.putText(frame, f'Mesafe: {distance_cm:.2f} cm', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    end_time = time.time()
    elapsed_time = end_time - start_time
    fps = 1 / elapsed_time
    start_time = end_time

    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
