from PIL import Image
from PIL import ImageFilter
from pylab import *

im0  = Image.open('images/knife_311.jpg')
figure(figsize =(8,8))

subplot(3,4,1)
plt.imshow(im0)
plt.title('Original')

#subplot(3,4,3)
#im2 =  im0.filter(ImageFilter.CONTOUR)
#plt.imshow(im2)
#plt.title('Contour')

#subplot(3,4,3)
#im3 =  im0.filter(ImageFilter.DETAIL)
#plt.imshow(im3)
#plt.title('Detail')

subplot(3,4,6)
im4  = im0.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(im4)
plt.title('Edge Enhance')

subplot(2,5,8)
im5 = im0.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(im5)
plt.title('Image Edge Enhance More')

#subplot(3,4,9)
#im6 = im0.filter(ImageFilter.EMBOSS)
#plt.imshow(im6)
#plt.title('Emboss')

#subplot(3,4,9)
#im7 =  im0.filter(ImageFilter.FIND_EDGES)
#plt.imshow(im7)
#plt.title('Find Edges')

#subplot(3,4,8)
#im8 =  im0.filter(ImageFilter.SMOOTH)
#plt.imshow(im8)
#plt.title('Lowpass 1')

#subplot(3,4,9)
#im9 =  im0.filter(ImageFilter.SMOOTH_MORE)
#plt.imshow(im9)
#plt.title('Lowpass 2')

subplot(3,4,11)
im10 = im0.filter(ImageFilter.SHARPEN)
plt.imshow(im10)
plt.title('Sharpen')


plt.show()

#Custom kernels


#size = (3,3)
#kernel1  = [1,1,1,1,-1,1,-1,-1,-1]
#ker1 =  ImageFilter.Kernel(size,kernel1,scale=None,offset =0)
#subplot(3,4,11)
#im11  =  im0.filter(ker1)
#plt.imshow(im11)
#plt.title('Custom Filter 1')


#kernel2 = [1,0,-1,1,0,-1,0,0,-1]
#ker2 = ImageFilter.Kernel(size,kernel2,scale =None,offset=0)
#subplot(3,5,12)
#im12 =  im0.filter(ker2)
#plt.imshow(im12)
#plt.title('Custom filter 2')


