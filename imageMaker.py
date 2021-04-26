import cv2
import numpy as np

hight = 768
width = 1024
img = np.zeros((hight, width))

# Change every pixel to 100
for i in range(hight):
    for j in range(width):
        img[i][j] = 100

cv2.imwrite("gray_100_image.jpg", img)
