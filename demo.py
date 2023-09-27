import cv2
import numpy as np

def find_black_coordinates(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    black_coordinates = []

    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            if pixel == 0:  # Siyah pikseli bulduğumuzda
                black_coordinates.append([x, y])  # Koordinatları listeye ekle
                return black_coordinates  # İlk siyah piksel bulundu, işlemi sonlandır

    return None  # Siyah piksel bulunamadı

def draw_circle_around_point(image_path, point_coordinates):
    image = cv2.imread(image_path)
    radius = 10
    color = (0, 0, 255)
    center = tuple(point_coordinates)

    cv2.circle(image, center, radius, color, -1)
    cv2.imshow("Resim", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "images/image2.jpeg"
black_coordinates = find_black_coordinates(image_path)

if black_coordinates is not None:
    print("İlk siyah pikselin koordinatları:")
    print(black_coordinates)

    first_black_pixel = black_coordinates[0]
    draw_circle_around_point(image_path, first_black_pixel)
else:
    print("Siyah piksel bulunamadı.")
