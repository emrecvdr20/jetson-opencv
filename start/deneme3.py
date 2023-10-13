import cv2
import numpy as np

def detect_red_in_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Treshold uygula
        _, thresholded = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        # Konturları bul
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Siyah nesneleri çevrele
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            print(x)
            print(y)
            print("*********")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255, 0), 2)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/video.mp4"
detect_red_in_video(video_path)
