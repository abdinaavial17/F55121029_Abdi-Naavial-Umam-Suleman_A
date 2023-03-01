import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)

hist, bins = np.histogram(img.flatten(), 256, [0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * float(hist.max()) / cdf.max()

img_equalized = np.interp(img.flatten(), bins[:-1], cdf_normalized).reshape(img.shape)

plt.imshow(img_equalized, cmap='gray')
plt.show()