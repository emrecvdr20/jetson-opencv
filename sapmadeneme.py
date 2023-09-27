import cv2
import numpy as np

def find_red_coordinates(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    red_pixels = cv2.bitwise_and(image, image, mask=mask)
    red_coordinates = np.column_stack(np.where(mask > 0))
    return red_coordinates

image_path = "images/image1.jpeg"
red_coordinates = find_red_coordinates(image_path)

print("Kırmızı renklerin koordinatları:")
for coordinate in red_coordinates:
    print(coordinate)
