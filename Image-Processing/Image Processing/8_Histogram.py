from PIL import Image
from pylab import *

img = Image.open('images/knife_1138.jpg').convert('L')
img_array = array(img)
#img.show()

figure()
hist(img_array.flatten(),500)
show()
