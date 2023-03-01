import cv2

img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('abdi.jpeg')

img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

diff_img = cv2.absdiff(img1, img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
