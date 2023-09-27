import cv2
import numpy as np

def find_black_coordinates(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    black_coordinates = []

    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            if pixel == 0:  
                black_coordinates.append([x, y])  
                return black_coordinates  

    return None  

def draw_circle_around_point(image, point_coordinates):
    radius = 10
    color = (0, 0, 255)
    center = tuple(point_coordinates)

    cv2.circle(image, center, radius, color, -1)


image1_path = "images/image1.jpeg"
image1 = cv2.imread(image1_path)
black_coordinates1 = find_black_coordinates(image1_path)

if black_coordinates1 is not None:
    print("İlk resimdeki ilk siyah pikselin koordinatları:")
    print(black_coordinates1)

    first_black_pixel1 = black_coordinates1[0]
    draw_circle_around_point(image1, first_black_pixel1)
else:
    print("İlk resimde siyah piksel bulunamadı.")


image2_path = "images/image2.jpeg"
image2 = cv2.imread(image2_path)
black_coordinates2 = find_black_coordinates(image2_path)

if black_coordinates2 is not None:
    print("İkinci resimdeki ilk siyah pikselin koordinatları:")
    print(black_coordinates2)

    first_black_pixel2 = black_coordinates2[0]
    draw_circle_around_point(image2, first_black_pixel2)
else:
    print("İkinci resimde siyah piksel bulunamadı.")

conversion_factor = 0.026

if black_coordinates1 is not None and black_coordinates2 is not None:
    first_coordinates_diff = np.subtract(black_coordinates1[0], black_coordinates2[0])
    print("İlk resimdeki koordinat - İkinci resimdeki koordinat:")
    print(first_coordinates_diff)

    first_coordinates_diff_cm = first_coordinates_diff * conversion_factor
    print("Sonuç:", first_coordinates_diff_cm,"cm")
else:
    print("Koordinatlar alınamadı.")

combined_image = np.vstack((image1, image2))
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
