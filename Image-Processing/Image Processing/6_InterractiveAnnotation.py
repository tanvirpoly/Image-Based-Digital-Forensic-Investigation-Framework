from PIL import Image
from pylab import *

im = array(Image.open('images/knife_1138.jpg'))
imshow(im)
#Select 5 points
pt = ginput(5)

print('You selected : ',pt)

show()
