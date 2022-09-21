# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
img = cv2.imread('images/2chestxray.jpg', 0)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
