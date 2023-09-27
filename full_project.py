import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('videos/myCam.mp4')  # Video dosyasının adını uygun şekilde değiştirin

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Çizgi bölgesini belirleme
        top_left = (100, 200)  # Üst sol köşenin koordinatları
        bottom_right = (200, 400)  # Alt sağ köşenin koordinatları
        region_of_interest = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

        # Mavi ve yeşil renklerin sayısını hesaplama
        blue_pixels = np.sum(region_of_interest[:, :, 0] > 0)
        green_pixels = np.sum(region_of_interest[:, :, 1] > 0)

        # Sonuçları ekranda gösterme
        result_frame = frame.copy()
        cv2.rectangle(result_frame, top_left, bottom_right, (0, 255, 0), 2)  # Yeşil dikdörtgen
        cv2.putText(result_frame, f"Blue Pixels: {blue_pixels}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(result_frame, f"Green Pixels: {green_pixels}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Color Analysis', result_frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
