import cv2
import numpy as np

def detect_green_in_center(video_path):
    cap = cv2.VideoCapture(video_path)

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 800, 600)

    while cap.isOpened():
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([60, 100, 100])
        upper_green = np.array([120, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        height, width, _ = frame.shape
        center_x = int(width / 2)
        center_y = int(height / 2)

        rect_size = 150

        cv2.rectangle(frame, (center_x - rect_size, center_y - rect_size), (center_x + rect_size, center_y + rect_size), (255, 255, 0), 2)

        center_mask = np.zeros_like(mask)
        center_mask[center_y - rect_size:center_y + rect_size, center_x - rect_size:center_x + rect_size] = mask[center_y - rect_size:center_y + rect_size, center_x - rect_size:center_x + rect_size]

        contours, _ = cv2.findContours(center_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            print(f"Yeşil nesne bulundu: X={x}, Y={y}, Genişlik={w}, Yükseklik={h}")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/AVI28.avi"
detect_green_in_center(video_path)
