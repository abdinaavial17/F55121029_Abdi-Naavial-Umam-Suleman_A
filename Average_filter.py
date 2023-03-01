import numpy as np
import cv2

img = cv2.imread('lena.jpg')

kernel_size = 3

kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

filtered_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Filtered', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
