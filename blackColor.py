import cv2
import numpy as np
import random

def draw_circle_around_point(image_path, point_coordinates):
    image = cv2.imread(image_path)
    radius = 10
    color = (0, 0, 255)

    for coordinates in point_coordinates:
        center = tuple(coordinates[::-1])
        cv2.circle(image, center, radius, color, -1)

    cv2.imshow("Resim", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "images/image2.jpeg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
black_coordinates = np.column_stack(np.where(gray_image == 0))

if len(black_coordinates) > 0:
    random_black_point = random.choice(black_coordinates)
    draw_circle_around_point(image_path, [random_black_point])
else:
    print("Siyah piksel bulunamadı.")
