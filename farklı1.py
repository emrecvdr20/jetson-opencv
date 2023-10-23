import cv2
import numpy as np

video = cv2.VideoCapture('videos/AVI11.avi')  

frame_width = int(video.get(3))
frame_height = int(video.get(4))
center_x = frame_width // 2
center_y = frame_height // 2

while True:
    ret, frame = video.read()

    if not ret:
        break

    color_at_center = frame[center_y, center_x]

    blue, green, red = color_at_center

    frame = cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    lower_red = np.array([160, 100, 20])
    upper_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(frame, lower_red, upper_red)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 500, 600)

    edges_red = cv2.bitwise_and(edges, edges, mask=red_mask)

    cv2.imshow('Kenarlar', edges_red)  

    print(f'Orta Nokta: ({center_x}, {center_y})')
    print(f'Renk (BGR): ({blue}, {green}, {red})')

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
