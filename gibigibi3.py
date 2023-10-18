import cv2
import numpy as np

def detect_black_line(video_path):
    cap = cv2.VideoCapture(video_path)   

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 800, 600)

    while cap.isOpened():
        ret, frame = cap.read()

        lower_black = np.array([0, 0, 0], dtype="uint8")
        upper_black = np.array([10, 10, 10], dtype="uint8")

        mask = cv2.inRange(frame, lower_black, upper_black)

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
            if w > 10 and h > 10:  # Sadece belirli bir boyuttaki nesneleri kabul et
                print(f"Siyah nesne bulundu: X={x}, Y={y}, Genişlik={w}, Yükseklik={h}")
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/AVI28.avi"
detect_black_line(video_path)
