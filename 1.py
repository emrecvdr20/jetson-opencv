import cv2
import numpy as np

def detect_red_objects(video_path):
    cap = cv2.VideoCapture(video_path)

    
    cv2.namedWindow("Original vs. Mask", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original vs. Mask", 800, 400)  

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

        combined_frame = np.hstack((frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)))

        cv2.imshow("Original vs. Mask", combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = "videos/video.mp4"
detect_red_objects(video_path)
