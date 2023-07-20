import cv2


image1 = cv2.imread('resources/cat.jpeg')
image2 = cv2.imread('resources/modiji.jpg')

# Resize image2 to match the size of image1
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Add two images (Pixel-wise addition)
result_addition = cv2.add(image1, image2)

# Subtract two images (Pixel-wise subtraction)
result_subtraction = cv2.subtract(image1, image2)

# Display the results
cv2.imshow('Image1', image1)
cv2.imshow('Image2', image2)
cv2.imshow('Addition', result_addition)
cv2.imshow('Subtraction', result_subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()
