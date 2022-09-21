import scipy.ndimage
from PIL import Image

a = Image.open('images/lena_noisy.png')

b =scipy.ndimage.filters.maximum_filter(a,size =5, footprint=None, output=None, mode ='reflect',cval=0.0,origin=0)
b = scipy.misc.toimage(b)
b.save('images/lena_max.png')
