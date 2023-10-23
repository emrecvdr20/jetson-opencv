import cv2
import numpy as np

cap = cv2.VideoCapture('videos/AVI7.avi')

lower_bound = np.array([165, 100, 100]) 
upper_bound = np.array([180, 255, 255]) 

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        height, width, _ = frame.shape

        print(height,width)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        center_y = height // 2
        center_x = width //2

        rect_width = 150
        rect_height = 150

        top_left = (width // 2 - rect_width // 2, height // 2 - rect_height // 2)
        bottom_right = (width // 2 + rect_width // 2, height // 2 + rect_height // 2)

        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)

        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                if top_left[0] < cX < bottom_right[0] and top_left[1] < cY < bottom_right[1]:
                    cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
                    cv2.putText(frame, f'Koordinatlar: ({cX}, {cY})', (cX + 10, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.line(frame, (0, center_y), (width, center_y), (0, 255, 0), 2)
        cv2.line(frame, (width // 2, 0), (width // 2, height), (0, 255, 0), 2)

        cv2.putText(frame, f'Merkez: ({center_x}, {center_y})', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
