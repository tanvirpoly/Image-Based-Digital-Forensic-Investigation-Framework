import numpy as np
import scipy.misc, math
from PIL import Image

img = Image.open('images/lena512.bmp')



img1 = scipy.misc.fromimage(img)
fl = img1.flatten()
hist, bins = np.histogram(img1,256,[0,255])

cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)

num_cdf_m = (cdf_m - cdf_m.min())*255
den_cdf_m  = (cdf_m.max()-cdf_m.min())

cdf_m  = num_cdf_m / den_cdf_m

cdf = np.ma.filled(cdf_m,0).astype('uint8')

im2 = cdf[fl]

im3 = np.reshape(im2,img1.shape)

im4 = scipy.misc.toimage(im3)

im4.show()
