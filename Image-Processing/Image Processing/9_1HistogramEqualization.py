import numpy as np
import cv2

# Load the image in greyscale
img = cv2.imread('images/pistol_81.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
out = clahe.apply(img)

# Display the images side by side using cv2.hconcat
out1 = cv2.hconcat([img,out])
cv2.imshow('a',out1)
cv2.waitKey(0)
