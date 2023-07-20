import cv2

# Load an image
image = cv2.imread('resources/cat.jpeg')

# Generate an image pyramid with 4 levels
pyramid = [image]
for i in range(4):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# Display the image pyramid
for i, level_image in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
