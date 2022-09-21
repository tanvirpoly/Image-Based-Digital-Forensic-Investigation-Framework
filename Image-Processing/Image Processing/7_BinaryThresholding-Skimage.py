from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *

from skimage import data
scanned =  data.page()

plt.imshow(scanned)
#plt.show()

#plt.imshow(scanned, cmap =cm.gray)
#plt.show()

thres =  np.zeros(shape(scanned)).astype('uint8')
threshold = 150
thres[scanned <threshold] =0
thres[scanned >=threshold] = 255

plt.imshow(thres, cmap=cm.gray)

plt.show()
