import cv2
import numpy as np

# Load an image
image = cv2.imread('resources/cat.jpeg')

# Resize the image to half of its original size using linear interpolation
resized_image = cv2.resize(image,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Make the resized image the same height as the original image
resized_image = cv2.copyMakeBorder(resized_image, 0, image.shape[0] - resized_image.shape[0], 0, 0, cv2.BORDER_CONSTANT)

# Display the original and resized images side by side
result = np.hstack((image, resized_image))
cv2.imshow('Image Resizing', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
