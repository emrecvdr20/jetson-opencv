import cv2


video_path = 'videos/AVI8.avi'  


cap = cv2.VideoCapture(video_path)




total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(total_frames)

current_frame = 0
while current_frame < total_frames:

    ret, frame = cap.read()


    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame', gray)

    key = cv2.waitKey(0)


    if key == ord('q'):
        break

    current_frame += 1

cap.release()

cv2.destroyAllWindows()
