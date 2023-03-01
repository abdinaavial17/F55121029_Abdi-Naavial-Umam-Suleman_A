import cv2
import numpy as np

img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('abdi.jpeg')

img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
