import cv2
import numpy as np

image1 = cv2.imread('images/image2.jpeg')
image2 = cv2.imread('images/image1.jpeg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

edges_image1 = cv2.Canny(gray_image1, 50, 150)

lines_image1 = cv2.HoughLinesP(edges_image1, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=5)

reference_line = lines_image1[0][0]

cv2.circle(image1, (reference_line[0], reference_line[1]), 5, (0, 0, 255), -1)

gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
edges_image2 = cv2.Canny(gray_image2, 50, 150)
lines_image2 = cv2.HoughLinesP(edges_image2, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=5)
detected_line = lines_image2[0][0]
cv2.circle(image2, (detected_line[0], detected_line[1]), 5, (0, 0, 255), -1)

horizontal_deviation = abs(reference_line[0] - detected_line[0])
point_distance = abs(reference_line[0] - detected_line[0])
line_distance = np.sqrt((reference_line[0] - detected_line[0])**2 + (reference_line[1] - detected_line[1])**2)

if detected_line[0] < reference_line[0]:
    image1, image2 = image2, image1
    reference_line, detected_line = detected_line, reference_line

distance_text = f"Mesafe: {horizontal_deviation} piksel"
cv2.putText(image2, distance_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.putText(image1, distance_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


cv2.line(image2, (reference_line[0], reference_line[1]), (detected_line[0], detected_line[1]), (0, 0, 255), 3)


# Kırmızıya kadar olan çizgi çizimi
cv2.line(image1, (reference_line[0], reference_line[1]), (detected_line[0], detected_line[0]), (0, 255, 0), 3)

scale_percent = 50
width = int(image1.shape[1] * scale_percent / 100)
height = int(image1.shape[0] * scale_percent / 100)
dim = (width, height)
image1_resized = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)
image2_resized = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Image 1', image1_resized)
cv2.imshow('Image 2', image2_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
