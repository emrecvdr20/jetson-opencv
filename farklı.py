import cv2

cap = cv2.VideoCapture('videos/AVI11.avi')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    center_x = frame.shape[1] // 2
    center_y = frame.shape[0] // 2

    yellow = (0, 255, 255)

    cv2.circle(frame, (center_x, center_y), 5, yellow, -1) 

    cv2.line(frame, (center_x, 0), (center_x, frame.shape[0]), (0, 0, 45), 2)
    cv2.line(frame, (0, center_y), (frame.shape[1], center_y), (0, 0, 45), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
