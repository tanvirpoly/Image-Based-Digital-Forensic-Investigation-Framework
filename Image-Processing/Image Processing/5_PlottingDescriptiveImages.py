from PIL import Image
from pylab import *

im = array(Image.open('images/knife_311.jpg'))
imshow(im)
#show()

x = [610,780,800,610]
y = [480,400,240,310]

#plot(x,y,'r*')


plot(x[:2],y[:2],'r')

plot(x[2:],y[2:],'r:')

#title('Plotting "pistol_64.jpg"')

show()
