from PIL import Image
from PIL import ImageFilter
from pylab import *

im0  = Image.open('images/knife_311.jpg')
figure(figsize =(12,6))

subplot(2,4,1)
plt.imshow(im0)
plt.title('Original')



subplot(2,4,2)
im1  = im0.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(im1)
plt.title('Edge Enhance')

subplot(2,4,3)
im2 = im0.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(im2)
plt.title('Image Edge Enhance More')



subplot(2,4,4)
im3 = im0.filter(ImageFilter.SHARPEN)
plt.imshow(im3)
plt.title('Sharpen')


plt.show()




