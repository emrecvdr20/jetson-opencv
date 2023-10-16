import cv2
import numpy as np

def detect_red_in_center(video_path):
    cap = cv2.VideoCapture(video_path)

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 800, 600)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([160, 100, 100])
        upper_red = np.array([179, 255, 255])

        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask = cv2.bitwise_or(mask1, mask2)

        result = cv2.bitwise_and(frame, frame, mask=mask)

        height, width, _ = frame.shape
        center_x = int(width / 2)
        center_y = int(height / 2)
        cv2.rectangle(frame, (center_x - 100, center_y - 100), (center_x + 100, center_y + 100), (255, 0, 0), 2)

        center_mask = np.zeros_like(mask)
        center_mask[center_y - 100:center_y + 100, center_x - 100:center_x + 100] = mask[center_y - 100:center_y + 100, center_x - 100:center_x + 100]

        contours, _ = cv2.findContours(center_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            print(f"Kırmızı nesne bulundu: X={x}, Y={y}, Genişlik={w}, Yükseklik={h}")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        cv2.waitKey(100)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/AVI28.avi"
detect_red_in_center(video_path)
