import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('butterfly.jpeg')

print(type(img))
print(img.shape)
plt.imshow(img)