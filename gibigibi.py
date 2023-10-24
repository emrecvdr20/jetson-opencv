import cv2
import numpy as np

def detect_red_in_center(video_path):
    cap = cv2.VideoCapture(video_path)

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 800, 600)

    while cap.isOpened():
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])

        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask = cv2.bitwise_or(mask1, mask2)

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
            print(f"Kırmızı nesne bulundu: X={x}, Y={y}, Genişlik={w}, Yükseklik={h}")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

        cv2.imshow("Frame", frame)
        cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/AVI11.avi"
detect_red_in_center(video_path)