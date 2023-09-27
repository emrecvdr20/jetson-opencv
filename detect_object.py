import cv2
import numpy as np

def calculate_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))

def find_objects(frame, target_color):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_bound = np.array([target_color[0] - 10, 100, 100])
    upper_bound = np.array([target_color[0] + 10, 255, 255])
    
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    objects = []
    
    for contour in contours:
        M = cv2.moments(contour)
        
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            color = frame[cY, cX]
            distance = calculate_distance(color, target_color)
            
            objects.append({
                "color": color,
                "distance_to_black": distance,
                "position": (cX, cY)
            })
    
    return objects

def main():
    video_path = "videos/myCam.mp4"
    target_color = (0, 255, 0)

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        objects = find_objects(frame, target_color)

        for obj in objects:
            print("Renk:", obj["color"])
            print("Siyaha Mesafe:", obj["distance_to_black"])
            print("Konum:", obj["position"])
            print("-" * 30)
            text = f"Mesafe: {obj['distance_to_black']:.2f} birim"
            cv2.putText(frame, text, obj['position'], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
