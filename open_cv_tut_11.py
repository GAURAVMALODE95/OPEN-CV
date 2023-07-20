import cv2
import numpy as np


image = cv2.imread('resources/cat.jpeg')

# Create a circular mask (black background with white circle)
mask = cv2.circle(np.zeros(image.shape[:2], dtype=np.uint8), (240,240), 150, 255,-1)

# Apply bitwise AND to extract the circular region from the image
result_bitwise_and = cv2.bitwise_and(image, image, mask=mask)

# Display the result
cv2.imshow('Bitwise AND', result_bitwise_and)
cv2.waitKey(0)
cv2.destroyAllWindows()
